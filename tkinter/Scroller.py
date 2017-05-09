from tkinter import *

root = Tk()

root.title('Tkinter Scroll')
root.minsize(500, 400)
root.configure(bg='red')
lbl = Label(root, text='A Basic Window With with a Scroll') 
lbl.pack()


def sel(): 
   selection = "Value = " + str(var.get())
   label.config(text = selection)


var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)
button = Button(root, text="Get Scale Value", font='freesansbold, 14', command=sel)
button.pack(anchor=CENTER)
label = Label(root) 
label.pack()

exit_button = Button(root, text='Exit', fg='red', bg='black', font='freesansbold, 14', command=quit) 
exit_button.pack(side=BOTTOM)

root.mainloop() 
