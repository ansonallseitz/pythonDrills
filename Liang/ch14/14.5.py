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


        window.geometry("900x500")

        #lets try to create a frame.
        self.bottom_frame = Frame(window).grid(row=7, rowspan=6)
 
        #create the canvas 
        self.canvas = Canvas(window, width=700, height=400, bg="blue")
        self.canvas.grid(column=0, row=0, padx=100, pady=20, columnspan=8)


    
        BtshowResults = Button(self.bottom_frame, text ="Show Results", command = self.showResults).grid(column=3, row = 7)
        

        BtnBrowse = Button(self.bottom_frame, text="Browse", command =self.browseFile).grid(column=2, row =7)
        #create the buttons 
        self.EnterdFile = StringVar()
        Entry(self.bottom_frame, textvariable = self.EnterdFile).grid(column=1, row=7)
        Label(self.bottom_frame, text="Enter a filename").grid(column=0, row=7)



        window.mainloop()


    #browse file function 
    def browseFile(self):
        filenameForReading = askopenfilename()
        self.EnterdFile.set(filenameForReading)

    #show result function 
    def showResults(self):
        filenameForReading = self.EnterdFile.get()
        letterCount = {} #create empty dictionary 
        infile = open(filenameForReading, "r")
        for line in infile:
            self.processLine(line.lower(), letterCount)

        y = 10
        for ch, count in sorted(letterCount.items()):
            x=500          
            text = f'letter { ch} appears { count}times.'
            self.canvas.create_text(x, y, text=text, fill="black", font=('Helvetica 15 bold'))
            y+=20
            
        #self.canvas.create_oval(10, 10, 190, 90, fill = 'red')
        #letterCountString = ' '.join('%s=%s' % (k, v) for k, v in letterCount.items())
        #self.canvas.create_text(300, 50, text=letterCountString, fill="black", font=('Helvetica 15 bold'))

        
    def processLine(self, line, letterCount):
        line = self.replacePunction(line)
        for ch in line: 
            if ch in letterCount:
                letterCount[ch] +=1 
            else: 
                letterCount[ch] = 1



    #replaces punction with blank space

    def replacePunction(self, line):
        for ch in line:
           if not ch.isalpha():
                line = line.replace(ch, "")
        return line

    #def replacePunction(self, line):


 

LetterCounter()     