import re
import textwrap
from datetime import date

import networkx as nx
import plotly.graph_objects as go
import pydot
from django.db.models import Q

from wbportfolio.models import Portfolio, PortfolioPortfolioThroughModel

from .utils import networkx_graph_to_plotly


class PortfolioGraph:
    def __init__(self, portfolio: Portfolio, val_date: date, **graph_kwargs):
        self.graph = pydot.Dot("Portfolio Tree", strict=True, **graph_kwargs)
        self.discovered_portfolios = set()
        self.val_date = val_date
        self._extend_portfolio_graph(portfolio)

    @classmethod
    def _convert_to_multilines(cls, name: str) -> str:
        lines = textwrap.wrap(name, 30)
        return "\n ".join(lines)

    def _extend_parent_portfolios_to_graph(self, portfolio):
        for parent_portfolio, weighting in portfolio.get_parent_portfolios(self.val_date):
            if parent_portfolio.assets.filter(date=self.val_date).exists():
                self.graph.add_node(
                    pydot.Node(
                        str(parent_portfolio.id),
                        label=self._convert_to_multilines(str(parent_portfolio)),
                        shape="circle",
                        orientation="45",
                        style="solid",
                    )
                )
                self.graph.add_edge(
                    pydot.Edge(str(portfolio.id), str(parent_portfolio.id), label=f"{weighting:.2%}", style="dashed")
                )
                # composition_edges.append((str(portfolio.id), str(parent_portfolio.id)))
                self._extend_parent_portfolios_to_graph(parent_portfolio)
                self._extend_portfolio_graph(parent_portfolio)

    def _extend_child_portfolios_to_graph(self, portfolio):
        for child_portfolio in portfolio.get_child_portfolios(self.val_date):
            self.graph.add_node(
                pydot.Node(
                    str(child_portfolio.id),
                    label=self._convert_to_multilines(str(child_portfolio)),
                    shape="circle",
                    orientation="45",
                    style="solid",
                )
            )
            # self.graph.add_edge(pydot.Edge(str(child_portfolio.id), str(portfolio.id), label="child", style="dashed"))
            # composition_edges.append((str(child_portfolio.id), str(portfolio.id)))
            self._extend_child_portfolios_to_graph(child_portfolio)

    def _extend_portfolio_graph(self, portfolio):
        self.graph.add_node(
            pydot.Node(
                str(portfolio.id),
                label=self._convert_to_multilines(str(portfolio)),
                shape="circle",
                orientation="45",
                style="solid",
            )
        )

        self._extend_parent_portfolios_to_graph(portfolio)
        self._extend_child_portfolios_to_graph(portfolio)

        # composition_edges = []
        # if composition_edges:
        #     with self.graph.subgraph(label=f'composition_{portfolio.id}') as a:
        #         a.edges(composition_edges)
        #         a.attr(color='blue')
        #         a.attr(label='Portfolio Composition')
        self.discovered_portfolios.add(portfolio)

        for rel in PortfolioPortfolioThroughModel.objects.filter(
            Q(portfolio=portfolio) | Q(dependency_portfolio=portfolio)
        ):
            self.graph.add_node(
                pydot.Node(
                    str(rel.portfolio.id),
                    label=self._convert_to_multilines(str(rel.portfolio)),
                    shape="square",
                    orientation="45",
                    style="solid",
                )
            )
            self.graph.add_node(
                pydot.Node(
                    str(rel.dependency_portfolio.id),
                    label=self._convert_to_multilines(str(rel.dependency_portfolio)),
                    shape="square",
                    orientation="45",
                    style="solid",
                )
            )
            label = PortfolioPortfolioThroughModel.Type[rel.type].label
            if rel.dependency_portfolio.is_composition:
                label += " (Composition)"
            self.graph.add_edge(
                pydot.Edge(
                    str(rel.dependency_portfolio.id),
                    str(rel.portfolio.id),
                    label=label,
                    style="bold",
                )
            )
            if rel.portfolio.is_lookthrough and rel.type == PortfolioPortfolioThroughModel.Type.PRIMARY:
                self.graph.add_edge(
                    pydot.Edge(
                        str(rel.portfolio.id), str(rel.dependency_portfolio.id), label="Look-Through", style="dotted"
                    )
                )
            if rel.dependency_portfolio not in self.discovered_portfolios:
                self._extend_portfolio_graph(rel.dependency_portfolio)
            if rel.portfolio not in self.discovered_portfolios:
                self._extend_portfolio_graph(rel.portfolio)

    def to_string(self) -> str:
        return self.graph.to_string()

    def to_networkx(self) -> nx.Graph:
        return nx.drawing.nx_pydot.from_pydot(self.graph)

    def to_plotly(self, **kwargs) -> go.Figure:
        node_labels = {
            node.get_name(): node.obj_dict["attributes"].get("label", node.get_name())
            for node in self.graph.get_node_list()
        }
        return networkx_graph_to_plotly(self.to_networkx(), labels=node_labels, **kwargs)

    def to_svg(self) -> str:
        svg = self.graph.create_svg().decode("utf-8")
        svg_matches = re.findall(r"<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>", svg, flags=re.DOTALL)
        if svg_matches:
            return svg_matches[0]
        return svg
