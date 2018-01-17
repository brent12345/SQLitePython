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


def updateinfo():
    text = e1.get()
    label = Label(frame, text=text)
    label.pack()

def findinfo(rows):
    for row in rows:

if __name__ == '__main__':
    rows = create_connection("chinook.db")

#label = []
#for row in rows:
#    label = Label(root, text = row[1], anchor=W, justify=CENTER) 
#    label.pack(side="bottom")

e1 = Entry(frame , width=50)
e1.pack()  
blackbutton = Button(frame, text="FIND", background="black", fg="white", command=updateinfo)
blackbutton.pack( side = BOTTOM)

#menubar = Menu(frame, tearoff=0)
#menubar.pack(side = BOTTOM)

root.mainloop()