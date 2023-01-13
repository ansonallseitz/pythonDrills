#Anson Allseitz

from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from tkinter import filedialog



class CountLetters:
    def __init__(self): 
        window = Tk() # create window
        window.title("Occurance of letters")
        
        self.canvas = Canvas(window, width = 500, height = 300, 
           bg = "white" )
        self.canvas.pack()

        #place buttons/textbox in frame 
        frame = Frame(window)
        frame.pack()
        #create label and text buttons
        textLable = Label(frame, text = "Enter a file name: ").pack(side=LEFT)
        self.filename= StringVar()
        entryName = Entry(frame, width = 25, textvariable = self.filename).pack(side=LEFT)

        btBrowse = Button(frame, text = "Browse", command= self.openFile).pack(slde=LEFT)
        btDisplayResult = Button(frame, text = "Show Result", command= self.displayResults).pack(slde=LEFT)
        

        window.mainloop() #create event loop


   # def openFile(self): 
      
        #filename.set(self.selectedFile)
    
   # def drawlHistogram(self):

        
    def displayResults(self):
        infile = open(self.filename.get(), "r")
        self.DoComputerStuff(infile)

    
    def drawlHistogram(self, histogram):
        Canvas.delete("Bar")

        HistWidth = 450
        HistHeight = 275
        Canvas.create_line(0, 400, 500, 400  )

        barWidth = (HistWidth - 25)/ len(histogram)
        barHeight =( HistHeight - 15)/len(histogram)
       
        for i in range(26):
            letter = chr(97 + i)
            print(letter, histogram[letter])

        for j in range(len(histogram)):
            height = histogram[letter]*barHeight
            Canvas.create_rectangle(j*barWidth, HistHeight-height(j+1)*barWidth, HistHeight)


 #drawls line across total bottom

        #HistWidth = ## Somethning? 
        #HistHeight



    def DoComputerStuff(self, infile):

        filedata = infile.read()
        histogram = {}
        for i in range(26):
            histogram[chr(97 + i)] = 0
        for letter in filedata:
            letter = letter.lower()
            if letter in histogram:  # Ignore spaces, punctuation, numbers, etc.
                histogram[letter] += 1      
        self.drawlHistogram(histogram)



CountLetters()



