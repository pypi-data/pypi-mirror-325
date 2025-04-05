from datetime import date

from wbportfolio.pms.typing import Portfolio as PortfolioDTO


class AbstractRebalancingModel:
    def __init__(self, portfolio, trade_date: date, last_effective_date: date):
        self.portfolio = portfolio
        self.trade_date = trade_date
        self.last_effective_date = last_effective_date

    def is_valid(self) -> bool:
        return True

    def get_target_portfolio(self, **kwargs) -> PortfolioDTO:
        raise NotImplementedError()
