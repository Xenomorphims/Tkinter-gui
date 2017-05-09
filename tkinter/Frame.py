from tkinter import *  
root = Tk()

root.title('Tkinter GUI - By Xenorm')
root.minsize(400,400)
root.configure(bg='cyan3')
lbl = Label(root, text='A BASIC FRAME') 
lbl.pack()
frame = Frame(root) 
frame.pack()

bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM )  
redbutton = Button(frame, text="Red Button", fg="red") 
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown Button", fg="brown") 
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue Button", fg="blue") 
bluebutton.pack( side = LEFT )

blackbutton = Button(root, text="Black", fg="black") 
blackbutton.pack(anchor=CENTER)


root.mainloop() 
