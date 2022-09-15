
from tkinter import *


class LabelLoop():

    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Tic Tack Toe! Yay Lets do it!")
        window.geometry("350x450")
        #window.columnconfigure((1, 2, 3,), weight=1)
        #window.rowconfigure((1, 2, 3, 4), weight=1)

        photo_x = PhotoImage(file='x.png')
        photo_o = PhotoImage(file='o.png')
        for y in range(3):
            for x in range(3):
                if (x + y) % 2:
                    image = photo_x
                else:
                    image = photo_o

        x=0
        y=0

        firstLabelList = []
        for y in range(3):
            for x in range(3):
                label = Label(window, image=image)
                # text=f'Label {x}×{y}')

                #label = Label(window, text=f'Label {x}×{y}')
                firstLabelList.append(label)
                label.grid(row=y, column=x)



    #label = Label(window, image=image)

          

        def on_click():
             firstLabelList[6]['text'] = "Yay it worked!"
            


        changeBttn = Button(window, text="change", command=on_click).grid(row=5, column=0)

        #Here is the problem, how do you fix this? 
  

   
        window.mainloop()
    
LabelLoop()