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
    root2.geometry('300x300')
    root2.title("Learning Window Two")
    root2.mainloop()

def updateinfo():

    
    findinfo(rows)

def findinfo(rows):
    global newlabel
    global root2
    root2 = Tk()
    newlabel = Label()
    text = e1.get()
    for row in rows:
        
        result = re.search(text, row[1])
        if result:
             newlabel = Label(root2, text="true")
             newlabel = Label(root2, text=row[1])
        else:
            newlabel2 = Label(root2, text="false")

    newlabel.pack()
    newlabel2.pack()                       
        
    
if __name__ == '__main__':
    rows = create_connection("chinook.db")
    json = getjson()

#label = []
#for row in rows:
#    label = Label(root, text = row[1], anchor=W, justify=CENTER) 
#    label.pack(side="bottom")

e1 = Entry(frame , width=50)
e1.pack()  
blackbutton = Button(frame, text="FIND", background="black", fg="white", command=updateinfo)
blackbutton2 = Button(frame, text="New Window", background="black", fg="white", command=anotherwindow)
blackbutton.pack( side = BOTTOM, padx=10)
blackbutton2.pack( side = BOTTOM, padx=10)
close_button = Button(frame, text="Close", command=root.quit)
close_button.pack()
#menubar = Menu(frame, tearoff=0)
#menubar.pack(side = BOTTOM)


root.mainloop()
