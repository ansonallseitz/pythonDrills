#9.6(Game: display a tic-tac-toe board ) Write a program that displays nine labels. 
# Each label may display an image icon for an X or an image icon for an O, as shown in Figure 9.25b. What to display is randomly decided. '
# Use the random.randint(0, 1)function to generate an integer 0 or1, which corresponds to displaying a cross image (X) icon or a not image (O) icon. 
# The cross and not images are in the files x.gif and o.gif.


#so the first thing I want to do
#is create the window, then wrtie a loop to generate the labels. I'm insistant on this method instadn of individually assigning them. 

from tkinter import *
from tkinter import ttk

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

        labelList1= [0]*3

        #ok, so i have a proof of concept, I can create labels using a loop. 
        #The next thing I want to do is prove that I can add logic to the labels, so I want to make a button
        #that changes the third one. 
    
        for i in range (3):
            labelList1[i]=Label(window, text=f"label {i}").grid(row=x, column=y) 
            x+=1
            


        changeBttn = Button(window, text="change", command=on_click).grid(row=5, column=0)


   
        window.mainloop()
    
TickTackToeTk()