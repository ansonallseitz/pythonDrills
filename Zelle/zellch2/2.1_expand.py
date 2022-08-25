#modify the the 2.1 program to be part of a gui. 
#This is an emotionally abusive program, that berates you 
#while converting temperature from Celsius to Freedom Units. 
#With a Gui! 


from tkinter import * 

class FuckingCelsius:
    def __init__(self):
        window = Tk() 
        window.title("Fucking Celsius")
        Label(window, text = "Hey Asshat\n").pack()
        Label(window, text = "This is the fucking tempetaure converstion program").pack( expand = 2)
        Label(window, text = "Enter a tempetaure in stupid Celsius").pack()
        Label(window, text = "And I will convert it to freedom units").pack()
        Label(window, text = "Fucking Celsius:  ").pack(side =LEFT )
        #Entry(window, textvariable = self.CelsiusEntry).pack(side = LEFT)
        self.celsiusEntry = IntVar()
        Entry(window, textvariable= self.celsiusEntry).pack(side = LEFT)
        Label(window, text = " Freedom Units: ").pack()
        #self.freedomUnits = 
       


        window.mainloop()

FuckingCelsius()