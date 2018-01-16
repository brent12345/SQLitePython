from tkinter import *
from SQLitePython import *


root = Tk()
root.geometry('300x300')
root.title("Learning")
frame = Frame(root)
frame.pack()

#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = RIGHT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = RIGHT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = RIGHT)

blackbutton = Button(frame, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

if __name__ == '__main__':
    rows = create_connection("chinook.db")
count = 1
label = []
for row in rows:
    row += row 
    count = count + 1
    label = Label(root, text = row[1], anchor=W, justify=CENTER) 
    
    label.pack(side="bottom")
#menubar = Menu(frame, tearoff=0)
#menubar.pack(side = BOTTOM)

root.mainloop()