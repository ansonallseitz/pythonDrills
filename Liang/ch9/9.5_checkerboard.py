#write a program that displays a 10x10 checkerboard with alternating white/black squares. 

from tkinter import *

class CheckerboardDemo:
    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Checkerboard Demo")

        #create frame & place in canvas 

        self.canvas = Canvas(window, width = 2000, height = 2000, bg = "#D3D3D3")
        self.canvas.pack()

        for y in range(10):
            for x in range(10):
                 self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20,)


        window.mainloop()

CheckerboardDemo()


