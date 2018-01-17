from tkinter import *
from SQLitePython import *
import re

root = Tk()
root.geometry('300x300')
root.title("Learning")
frame = Frame(root)
frame.pack()

#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )
def anotherwindow():
    root2 = Tk()
    root2.geometry('300x300')
    root2.title("Learning Window Two")
    root.mainloop()

def updateinfo():
    text = e1.get()
    label.pack()
    findinfo(rows)

def findinfo(rows):
    text = e1.get()
    for row in rows:
        result = re.search(text, row[1])
        if result:
             newlabel = Label(frame, text="true")
             newlabel.pack()            
        
    
if __name__ == '__main__':
    rows = create_connection("chinook.db")

#label = []
#for row in rows:
#    label = Label(root, text = row[1], anchor=W, justify=CENTER) 
#    label.pack(side="bottom")

e1 = Entry(frame , width=50)
e1.pack()  
blackbutton = Button(frame, text="FIND", background="black", fg="white", command=updateinfo)
blackbutton2 = Button(frame, text="New Window", background="black", fg="white", command=anotherwindow)
blackbutton.pack( side = BOTTOM)
blackbutton2.pack( side = BOTTOM)

#menubar = Menu(frame, tearoff=0)
#menubar.pack(side = BOTTOM)


root.mainloop()