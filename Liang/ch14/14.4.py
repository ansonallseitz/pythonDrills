from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

class LetterCounter():

    def __init__(self):
        #create the window
        window=Tk()
        window.title("Occurance Of Letters")
        window.columnconfigure((1,2,3,4,5,6,7,8,9,10), weight=1)
        window.rowconfigure((1,2,3,4,5,6,7), weight =1)


        window.geometry("475x350")
 
        #create the canvas 
        self.canvas = Canvas(window, width=200, height=200, bg="blue")
        self.canvas.grid(column=0, row=0)

        BtshowResults = Button(window, text ="Show Results", command = self.showResults).grid(column=9, row = 7)
        BtnBrowse = Button(window, text="Browse", command =self.browseFile).grid(column=7, row =7)
        #create the buttons 
        self.EnterdFile = StringVar()
        Entry(window, textvariable = self.EnterdFile).grid(column=4, row=7)
        Label(window, text="Enter a filename").grid(column=0, row=7)



        window.mainloop()


    #brows file function 
    def browseFile(self):
        filenameForReading = askopenfilename()
        self.EnterdFile.set(filenameForReading)
    
    #show result function 
    def showResults(self, filenameForReading):
        letterCount = {} #create empty dictionary 
        filenameForReading 

 

LetterCounter()     