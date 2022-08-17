#write a program that displays a 10x10 checkerboard with alternating white/black squares. 

from tkinter import *

class CheckerboardDemo:
    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Checkerboard Demo")

        #create frame & place in canvas 

        self.canvas = Canvas(window, width = 800, height = 750, bg = "#D3D3D3")

        window.mainloop()

CheckerboardDemo()


