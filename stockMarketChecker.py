from polygon import RESTClient
import json
from urllib3 import HTTPResponse
from typing import cast
import sys



polygoneKey = "9jWas5pTeCmLZ0nzngQ93nhHe35PN_eu"

def getStockAnalysis(stockSymbol, startDate, endDate):
    client = RESTClient(polygoneKey)

    aggregates = cast(HTTPResponse, client.get_aggs(stockSymbol, 1, 'day', startDate, endDate, raw=True, sort='desc'))

    data = json.loads(aggregates.data)
    highestPrices = []
    lowestPrices = []
    for item in data:
        if item == 'results':
            for element in range(len(data[item])):
                highestPrices.append(data[item][element]['h'])
                lowestPrices.append(data[item][element]['l'])
                print(f"Day {element+1} : ")
                print(f"estimated price : {data[item][element]['c']}")
                print(f"highest price : {data[item][element]['h']}")
                print(f"lowest price : {data[item][element]['l']}")
                print('\n')
    print(f'highest price over this period : {max(highestPrices)}')
    print(f'lowest price over this period : {min(lowestPrices)}')
if __name__ == "__main__":
    try:
        getStockAnalysis(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        print("wrong argument format. please enter the argument in the follwoing format : stock_symbol (ex: AAPL) start_date (ex: 2023-05-22) end_date (ex: 2023-05-23)")