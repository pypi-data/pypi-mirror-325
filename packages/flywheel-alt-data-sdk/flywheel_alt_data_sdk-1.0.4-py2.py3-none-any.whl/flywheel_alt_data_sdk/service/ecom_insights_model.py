import requests
import json
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import enum
# [{'BLOOMBERG_ID': 'LULU US', 'METRIC': 'TOTAL_wgtavgprice_total_instock_wholesale', 'WEEK_START_DATE': 1732492800000, 'VALUE': 100.5477408568}]

@dataclass
class EcomInsightsMetricMonthly:

    BLOOMBERG_ID: str
    MONTH_START_DATE: int
    PRODUCT_GROUP: str
    SEGMENT: str
    CHANNEL: str
    AVGPRICE_TOTAL_TOTAL: float
    AVGPRICE_TOTAL_INSTOCK: float
    AVGPRICE_MARKDOWN_INSTOCK: float
    AVGPRICE_MARKDOWNLIST_INSTOCK: float
    AVGPRICE_LIST_INSTOCK: float
    MARKDOWN_BREADTH_INSTOCK: float
    AVGDISCOUNT_INSTOCK: float
    AGGDISCOUNT_INSTOCK: float
    AVGDAILYSKUS_TOTAL_TOTAL: float
    AVGDAILYSKUS_TOTAL_INSTOCK: float
    AVGDAILYSKUS_MARKDOWN_INSTOCK: float
    AVGDAILYPRODUCTS_TOTAL_TOTAL: float
    AVGDAILYPRODUCTS_TOTAL_INSTOCK: float
    INSTOCK_RATE: float
    SKUS_PER_PRODUCT: float
    WGTAVGPRICE_TOTAL_INSTOCK: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
@dataclass
class EcomInsightsMetricWeekly:

    BLOOMBERG_ID: str
    WEEK_START_DATE: int
    PRODUCT_GROUP: str
    SEGMENT: str
    CHANNEL: str
    AVGPRICE_TOTAL_TOTAL: float
    AVGPRICE_TOTAL_INSTOCK: float
    AVGPRICE_MARKDOWN_INSTOCK: float
    AVGPRICE_MARKDOWNLIST_INSTOCK: float
    AVGPRICE_LIST_INSTOCK: float
    MARKDOWN_BREADTH_INSTOCK: float
    AVGDISCOUNT_INSTOCK: float
    AGGDISCOUNT_INSTOCK: float
    AVGDAILYSKUS_TOTAL_TOTAL: float
    AVGDAILYSKUS_TOTAL_INSTOCK: float
    AVGDAILYSKUS_MARKDOWN_INSTOCK: float
    AVGDAILYPRODUCTS_TOTAL_TOTAL: float
    AVGDAILYPRODUCTS_TOTAL_INSTOCK: float
    INSTOCK_RATE: float
    SKUS_PER_PRODUCT: float
    WGTAVGPRICE_TOTAL_INSTOCK: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

def stream_api(api_key:str, ticker: str, report_frequency: str):
    """
    Connects to the streaming API and processes incoming data.
    """
    try:
        with requests.post(
            "https://ecom-api.ad.flywheeldigital.com/stream",
            data=json.dumps({"ticker": ticker, "report_frequency": report_frequency}),
            headers={"Content-Type": "application/json",
                     "x-api-key": api_key},
            timeout=None,
        ) as response:
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                print(response.text)
                return
            x = response.json()
            results = []
            if report_frequency == "WEEKLY":
                for i in x:
                    ecom_insight = EcomInsightsMetricWeekly(**i)
                    results.append(ecom_insight)
                return results
            else:
                for i in x:
                    ecom_insight = EcomInsightsMetricMonthly(**i)
                    results.append(ecom_insight)
            return results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
