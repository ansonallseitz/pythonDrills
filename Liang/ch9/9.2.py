#(Create an investment-value calculator) Write a program that calculates the future value of an investment 
#at a given interest rate for a specified number of years. The formula for the calculation is as follows:


#futureValue = investmentAmount * (1 + monthlyInterestRate)^(years * 12)
from tkinter import *

class InvestmentCalc():
    def __init__(self): 
        window = Tk() #create a window 
        window.title("Investment Calculator")
        window.geometry("400x400")
        window.columnconfigure((1,2,3,4), weight=1)
        window.rowconfigure((1,2,3,4), weight =1)

        #first we make the labels   
        Label(window, text ="Investment Amount: ").grid(row =1, column=1, sticky=W)
        Label(window, text="monthly Intrest Rate").grid(row=2, column=1, sticky=W)
        Label(window, text ="years:").grid(row=3, column=1, sticky=W)
        Label(window, text ="final value of Investment: ").grid(row=4, column=1, sticky=W)

        #next we make the text entries. 
        self.investmentEntry = StringVar()
        Entry(window, textvariable= self.investmentEntry, justify=RIGHT).grid(row=1, column=2, sticky=E)
        self.intrestRateEntry= StringVar()
        Entry(window, textvariable=self.intrestRateEntry, justify=RIGHT).grid(row=2, column=2, sticky=E)
        self.yearsEntry = StringVar()
        Entry(window, textvariable=self.yearsEntry, justify=RIGHT).grid(row=3, column=2, sticky=E)

        self.totalInvestment = StringVar()
        LabelTotalInvestment = Label(window, textvariable=self.totalInvestment).grid(row=4, column=2, sticky=E)
        btComputeInvestment=Button(window, text= "Compute_Investment", command =self.computeInvestment).grid(row=5, column=3, sticky=E)

        window.mainloop()

    def computeInvestment(self):
        futureInvestmentValue = self.getInvestmentValue(float(self.investmentEntry.get()), float(self.intrestRateEntry.get())/100, int(self.yearsEntry.get()))

        self.totalInvestment.set(format(futureInvestmentValue, '10.2f' ))



    def getInvestmentValue(self, investmentAmount, monthlyIntrestRate, numberOfYears):  
        futureInvestmentValue= investmentAmount * (1+ monthlyIntrestRate)**(numberOfYears * 12)
        return futureInvestmentValue



InvestmentCalc()