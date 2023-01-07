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
       # self.canvas = Canvas(window, width=200, height=200, bg="blue").grid(column=0, row=0)
        #self.canvas.pack()
        
        self.canvas = Canvas(window, width=200, height=200, bg="blue")
        self.canvas.grid(column=0, row=0)

        BtshowResults = Button(window, text ="Show Results", command = self.showResults).grid(column=9, row = 7)
        BtnBrowse = Button(window, text="Browse", command =self.browseFile).grid(column=7, row =7)
        #BtshowResults.pack()
        self.EnterdFile = StringVar()
        fileEntry = Entry(window, textvariable = self.EnterdFile).grid(column=4, row=7)
        Label(window, text="Enter a filename").grid(column=0, row=7)

        window.mainloop()

    def showResults(self):
        self.canvas.create_rectangle(75, 70, 150, 150, fill="red")
   # def browse(self):
      #  self.canvas.create_oval(75, 40, 112, 90, fill="purple")
    
    def browseFile(self):
        filenameForReading = askopenfilename()
        

 

LetterCounter()