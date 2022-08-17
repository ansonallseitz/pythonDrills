#Write a program that moves a ball in a panel 
#you shoudl define a panel calss for displaying the ball and provide the 
#methogs for movign the bal to the left, rignt up and down


#Step 1, define the window, step 2 define the buttons. 
#step #3 create logic to make circle appear. 
from bisect import bisect_left
from tkinter import *

class BallDemo: 
    def __init__(self): 
        window = Tk()
        window.title("Move The ball around")

        #place canvas in frame 
        self.canvas = Canvas(window, width = 400, height = 350, bg = "white")
        self.canvas.pack()
        #place buttons in frame 
        frame = Frame(window)
        frame.pack()

        btLeft = Button(frame, text = "Left", command = self.displayLeft)
        btRight = Button(frame, text = "Right", command = self.displayRight)
        btUp = Button(Frame, text = "Up", command = self.displayUp)
        BtDown = Button(Frame, text = "down", command = self.displayDown)


        btLeft.grid(row =1, column = 1)
        btRight.grid(row =1, column =2)
        btUp.grid(row =1, column =3)
        BtDown.grid(row =1, column =4)

        window.mainloop() # Create an event loop

        def displayLeft(self):
            self.canvas.create_oval(20, 20, 23, 23, fill = "blue", tags = "left")
        def displayRight(self):
            self.canvas.create_oval(20, 70, 23, 73, fill = "blue", tags = "left")
        def displayUp(self):
            self.canvas.create_oval(5, 10, 8, 13, fill = "blue", tags = "left")
        def displayDown(self):
            self.canvas.create_oval(40, 10, 43, 13, fill = "blue", tags = "left")


BallDemo()