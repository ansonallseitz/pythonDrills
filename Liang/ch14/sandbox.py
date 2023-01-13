
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

def __init__(self,root):
    self.BuildMainWindow(root)
    self.ListboxSet = 0 
    return

#displays the menu bar and options
def BuildMainWindow(self, root):
    menubar = Menu(root)
    root.config(menu=menubar)

    # Create a menu button labeled "File" that brings up a menu
    filemenu = Menu(menubar)
    menubar.add_cascade(label='File', menu=filemenu)

    # Create entries in the "File" menu
    # simulated command functions that we want to invoke from our menus
    filemenu.add_command(label='Open', command=self.openfile)
    filemenu.add_separator(  )
    filemenu.add_command(label='Quit', command=sys.exit)

#upon selecting a directory from the menu and listboxes/buttons are created
def BuildListbox(self, directory):
    self.listbox1 = Tkinter.Listbox()
    self.listbox2 = Tkinter.Listbox()
    self.listbox1.grid(row=1, column=1, rowspan = 4, columnspan = 5)
    self.listbox2.grid(row=1 ,column=15, rowspan = 4, columnspan = 5)
    self.listbox2.bind('<<ListboxSelect>>', lambda e:SortActions.GetWindowIndex(self,e))
    self.listbox2.bind('<B1-Motion>', lambda e:SortActions.MoveWindowItem(self,e))

    i = 0
    for filename in sorted(os.listdir(directory)):
        self.listbox1.insert(i, filename)
        i = i + 1

    self.bAddToListTwo = Button(text = "->", command = lambda:SortActions.AddToListTwo(self,self.listbox1.curselection()))
    self.bAddToListTwo.grid(row=1, column = 6)
    self.bAddAll = Button(text = "Add All To Playlist", command = lambda:SortActions.AddAllFiles(self))
    self.bAddAll.grid(row=2, column = 6)
    self.bRemoveFromListTwo = Button(text = "Remove From Playlist", command = lambda:SortActions.RemoveFromListTwo(self,self.listbox2.curselection()))
    self.bRemoveFromListTwo.grid(row=3, column = 6)
    self.bSavePlaylist = Button(text = "Save Playlist", command = lambda:SortActions.SaveList(self))
    self.bSavePlaylist.grid(row=4, column = 6)