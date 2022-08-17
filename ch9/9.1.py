#Write a program that moves a ball in a panel 
#you shoudl define a panel calss for displaying the ball and provide the 
#methogs for movign the bal to the left, rignt up and down


#Step 1, define the window, step 2 define the buttons. 
#step #3 create logic to make circle appear. 

from tkinter import *

class BallDemo: 
    def __init__(self): 
        window = Tk()
        window.title("Move The ball around")

        #place canvas in frame 
        self.canvas = Canvas(window, width = 400, height = 350, bg = "white")
        self.canvas.pack()
        #place buttons in frame 
        frame1 = Frame(window)
        frame1.pack()

        btLeft = Button(frame1, text = "Left", command = self.displayLeft)
        btRight = Button(frame1, text = "Right", command = self.displayRight)
        btUp = Button(frame1, text = "Up", command = self.displayUp)
        BtDown = Button(frame1, text = "down", command = self.displayDown)


        btLeft.grid(row =1, column = 1)
        btRight.grid(row =1, column =2)
        btUp.grid(row =1, column =3)
        BtDown.grid(row =1, column =4)


        window.mainloop() # Create an event loop

    def displayLeft(self):
        self.canvas.delete("left", "Right", "Up", "Down")
        self.canvas.create_oval(40, 150, 50, 160, fill = "#00FFFF", tags = "left")
    def displayRight(self):
        self.canvas.delete("left", "Right", "Up", "Down")
        self.canvas.create_oval(300, 150, 310, 160, fill = "#ff0000", tags = "Right")
    def displayUp(self):
        self.canvas.delete("left", "Right", "Up", "Down")
        self.canvas.create_oval(180, 20, 190, 30, fill = "#AFE1AF", tags = "Up")
    def displayDown(self):
        self.canvas.delete("left", "Right", "Up", "Down")
        self.canvas.create_oval(180, 250, 190, 260, fill = "#FFA500", tags = "Down")



BallDemo()