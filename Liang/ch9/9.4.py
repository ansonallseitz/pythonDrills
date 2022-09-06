#(Display rectangles) Write a program that displays 20 rectangles, as shown in Figure 9.24.

from tkinter import * 

class RectangleLoop():

    def __init__(self): 
        #create the window
        window =Tk()
        window.title("Concentric rectangles")

        self.canvas = Canvas(window, width=1000, height =1000)
        self.canvas.pack()

        self.x1 = 500
        self.y1 = 500
        self.x2 = 600
        self.y2 = 510

       # self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2)

        for x in range(20):
            self.canvas.create_rectangle( 
            self.x1 -(x*20), self.y1 -(x*20), self.x2 +(x*20), self.y2 + (x*20))



        window.mainloop()

RectangleLoop()

    
        

