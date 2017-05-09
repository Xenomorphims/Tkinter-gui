from Tkinter import *

root = Tk()
root.minsize(800, 400)
root.option_readfile('optionDB')
root.title('Radiobutton')

cheese = [('Innocent', 1), ('Yvonne', 2), ('Mulenga', 3),
          ('Penyani', 4), ('Judith', 5), ('John', 6)]

var = IntVar()

for text, value in cheese:
    Radiobutton(root, text=text, value=value, variable=var, indicatoron=0).pack(anchor=W, fill=X, ipadx=18)

var.set(3)

root.mainloop()
