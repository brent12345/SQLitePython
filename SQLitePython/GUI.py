from tkinter import *

root = Tk()
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

root.mainloop()