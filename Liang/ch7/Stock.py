#(The Stock class) Design a class named Stock to represent a company’s stock
#that contains:
#■ A private string data field named symbol for the stock’s symbol.
#■ A private string data field named name for the stock’s name.
#■ A private float data field named previousClosingPrice that stores the stock
#price for the previous day.
#■ A private float data field named currentPrice that stores the stock price for
#the current time.
#■ A constructor that creates a stock with the specified symbol, name, previous
#price, and current price.
#■ A get method for returning the stock name.
#■ A get method for returning the stock symbol.
#■ Get and set methods for getting/setting the stock’s previous price.
#■ Get and set methods for getting/setting the stock’s current price.
#■ A method named getChangePercent() that returns the percentage changed
#from previousClosingPrice to currentPrice.
#Draw the UML diagram for the class, and then implement the class. Write a test
#program that creates a Stock object with the stock symbol INTC, the name Intel
#Programming Exercises 237
#Corporation, the previous closing price of 20.5, and the new current price of
#20.35, and display the price-change percentage.
#'''


class Stock:
    #construct the stock object
    def __init__(self, symbol = "XXXX", stockName = "default", previousClosingPrice=0.00, currentPrice = 0.00):
        self.__symbol = symbol
        self.__stockName = stockName
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    

    def getStockSymbol(self):
        return self.__symbol

    def getStockName(self):
        return self.__stockName
    
    def getCurrentPrice(self):
        return self.__currentPrice

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def setCurrentPrice(self, __currentPrice):
        self.currentPrice = __currentPrice
    
    def setPreviousColsingPrice(self, __previousClosingPrice): 
        self.previousClosingPrice = __previousClosingPrice

    def getChagePercent(self):
        changePercent = (self.currentPrice - self.previousClosingPrice) / self.previousClosingPrice * 100
        return changePercent




from Stock import Stock


def main():

    stock = Stock("INTC", "Intel", 20.5, 20.35 )

    print("The name of the stock is: ", stock.getStockName())
    print("The symbol of the stock is: ", stock.getStockSymbol())
    print("The previous closing price of the stock was: ", stock.getPreviousClosingPrice())
    print("The current price for the stock is: ", stock.getCurrentPrice())
    print("The percentage change of between the two prices are: ", stock.getChagePercent())
main() #call the main thingmajig



