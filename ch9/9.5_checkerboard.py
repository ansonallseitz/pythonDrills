#write a program that displays a 10x10 checkerboard with alternating white/black squares. 

from tkinter import *

class CheckerboardDemo:
    def __init__(self):
        #create the window 
        window =Tk()
        window.title("Checkerboard Demo")

        #create frame & place in canvas 

        self.canvas = Canvas(window, width = 800, height = 750, bg = "#D3D3D3")

        for y in range(10):
            for x in range(10):
                self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill='purple')

        window.mainloop()

CheckerboardDemo()


