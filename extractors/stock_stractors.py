import pandas as pd
import requests
import json
from pprint import pprint
from entities.constants import ExchangeRegion

token_path = "../data/token.json"


def stock_history(
        stock: str,
        size: int,
        exchange_region: ExchangeRegion = ExchangeRegion.SAO_PAULO
) -> pd.DataFrame:
    with open(token_path, 'r') as file:
        data = json.load(file)
        api_access = data['access_key']
    function = 'TIME_SERIES_DAILY'

    host = "www.alphavantage.co"
    url = f"https://{host}/query?function={function}&symbol={stock}.{exchange_region.value}"
    url += f"&apikey={api_access}&datatype=csv"
    response = requests.get(url)
    with open(f"{stock}.csv", 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print(response)



if __name__ == "__main__":
    # with open(token_path, 'r') as file:
    #     data = json.load(file)
    #     api_access = data['access_key']
    #
    # function = "SYMBOL_SEARCH"
    # equity_symbol = "microsoft"
    # interval = "60min"
    # keywords = "microsoft"
    # host = "www.alphavantage.co"
    # url = f"https://{host}/query?function={function}&keywords={equity_symbol}&apikey={api_access}"
    #
    # response = requests.get(url)
    # data = response.json()
    # pprint(data)

    stock_history('VALE3', 4)
