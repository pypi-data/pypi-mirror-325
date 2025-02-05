import requests
import json
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import enum
# [{'BLOOMBERG_ID': 'LULU US', 'METRIC': 'TOTAL_wgtavgprice_total_instock_wholesale', 'WEEK_START_DATE': 1732492800000, 'VALUE': 100.5477408568}]

@dataclass
class EcomInsightsMetric:
    # "BLOOMBERG_ID": "LULU US",
    # "MONTH_START_DATE": 1409529600000,
    # "PRODUCT_GROUP": "total",
    # "SEGMENT": "total",
    # "CHANNEL": "retail1p",
    # "AVGPRICE_TOTAL_TOTAL": 79.5461312753,
    # "AVGPRICE_TOTAL_INSTOCK": 79.5708415281,
    # "AVGPRICE_MARKDOWN_INSTOCK": 67.5344827586,
    # "AVGPRICE_MARKDOWNLIST_INSTOCK": 84.7931034483,
    # "AVGPRICE_LIST_INSTOCK": 81.5434814523,
    # "MARKDOWN_BREADTH_INSTOCK": 5.5012980591,
    # "AVGDISCOUNT_INSTOCK": 21.427099272,
    # "AGGDISCOUNT_INSTOCK": 1.0581114769,
    # "AVGDAILYSKUS_TOTAL_TOTAL": 5698.0,
    # "AVGDAILYSKUS_TOTAL_INSTOCK": 5392.6666666667,
    # "AVGDAILYSKUS_MARKDOWN_INSTOCK": 296.6666666667,
    # "AVGDAILYPRODUCTS_TOTAL_TOTAL": 389.5,
    # "AVGDAILYPRODUCTS_TOTAL_INSTOCK": 389.5,
    # "INSTOCK_RATE": 94.6413946414,
    # "SKUS_PER_PRODUCT": 14.6290115533,
    # "WGTAVGPRICE_TOTAL_INSTOCK": 73.8037149215
    
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
            
            for i in x:
                ecom_insight = EcomInsightsMetric(**i)
                results.append(ecom_insight)
                
            return results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
