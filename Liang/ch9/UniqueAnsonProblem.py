
from tkinter import *


class TickTackToeTk():

    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Tic Tack Toe! Yay Lets do it!")
        window.geometry("350x450")
        #window.columnconfigure((1, 2, 3,), weight=1)
        #window.rowconfigure((1, 2, 3, 4), weight=1)

     

        x=0
        y=0

        firstLabelList= [0]*3

        #ok, so i have a proof of concept, I can create labels using a loop. 
        #The next thing I want to do is prove that I can add logic to the labels, so I want to make a button
        #that changes the third one. 
    
        for i in range (3):
            firstLabelList[i]=Label(window, text=f"label {i}").grid(row=x, column=y) 
            x+=1
            


        changeBttn = Button(window, text="change", command=on_click).grid(row=5, column=0)

        #Here is the problem, how do you fix this? 
        def on_click():
            firstLabelList2.configure(text="This is updated Label text")
               

   
        window.mainloop()
    
TickTackToeTk()