import json
from contextlib import suppress
from datetime import datetime


def parse(import_source):
    data = []
    with suppress(KeyError):
        series_data = json.loads(import_source.file.read())["payload"]["series"]
        for series in series_data:
            isin = series["item"]["priceIdentifier"]
            for point in series["points"]:
                data.append(
                    {
                        "instrument": {"isin": isin},
                        "date": datetime.fromtimestamp(int(point["timestamp"]) / 1000).strftime("%Y-%m-%d"),
                        "net_value": point["close"],
                    }
                )
    return {"data": data}
