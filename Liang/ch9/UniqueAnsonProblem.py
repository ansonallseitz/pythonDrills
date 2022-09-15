
from tkinter import *


class LabelLoop():

    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Tic Tack Toe! Yay Lets do it!")
        window.geometry("350x450")
        #window.columnconfigure((1, 2, 3,), weight=1)
        #window.rowconfigure((1, 2, 3, 4), weight=1)

     

        x=0
        y=0

        firstLabelList = []
        for y in range(3):
            for x in range(3):
                label = Label(window, text=f'Label {x}×{y}')
                firstLabelList.append(label)
                label.grid(row=y, column=x)
          

        def on_click():
             firstLabelList[6]['text'] = "Yay it worked!"
            


        changeBttn = Button(window, text="change", command=on_click).grid(row=5, column=0)

        #Here is the problem, how do you fix this? 
  

   
        window.mainloop()
    
LabelLoop()