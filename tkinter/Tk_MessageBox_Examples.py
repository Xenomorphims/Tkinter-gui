from tkinter import *
import tkMessageBox
tkMessageBox.showinfo('Hi from Xenorm!', 'Hello humans!\n\nThis is a message box, by Xenorm.')
#or tkMessageBox.showwarning
#or tkMessageBox.askyesno
#or tkMessageBox.askokcancel
#or tkMessageBox.askretrycancel
#or tkMessageBox.askquestion
#or tkMessageBox.askinteger

from tkFileDialog import *
askopenfilename()
#or askdirectory()
#or asksaveasfilename()

from tkSimpleDialog import *
#or askinteger("The value","Enter a value") 

from tkColorChooser import *
#or tkMessageBox.askcolor() 
