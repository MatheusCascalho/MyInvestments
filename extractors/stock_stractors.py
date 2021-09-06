import requests
import json
from pprint import pprint


token_path = "../data/token.json"
with open(token_path, 'r') as file:
    data = json.load(file)
    api_access = data['access_key']

function = "SYMBOL_SEARCH"
equity_symbol = "microsoft"
interval = "60min"
keywords = "microsoft"
host = "www.alphavantage.co"
url = f"https://{host}/query?function={function}&keywords={equity_symbol}&apikey={api_access}"

response = requests.get(url)
data = response.json()
pprint(data)
