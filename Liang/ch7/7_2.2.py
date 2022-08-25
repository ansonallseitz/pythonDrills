#program that creates a Stock object with the stock symbol INTC, the name Intel
#Programming Exercises 237
#Corporation, the previous closing price of 20.5, and the new current price of
#20.35, and display the price-change percentage.
#'''

from Stock import Stock


def main():

    stock = Stock("INTC", "Intel", 20.5, 20.35 )

    print("The name of the stock is: ", stock.getStockName())
    print("The symbol of the stock is: ", stock.getStockSymbol())
    print("The previous closing price of the stock was: ", stock.getPreviousClosingPrice())
    print("The current price for the stock is: ", stock.getCurrentPrice())
    print("The percentage change of between the two prices are: ", stock.getChagePercent())
main() #call the main thingmajig

