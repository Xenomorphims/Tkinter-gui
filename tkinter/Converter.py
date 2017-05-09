import sys
from tkinter import *

def donothing(): 
   filewin = Toplevel(root) 
   button = Button(filewin, text="Do nothing button") 
   button.pack()
def mHello():
    mText=ment.get()
    mlabel1 = Label(root,text=mText).pack()

def myNew():
    mlabel1 = askdirectory()

def myOpen():
    myOpen = askopenfilename()
    mlabel4 = Label(root,text=myOpen).pack()

def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = tkMessageBox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        root.destroy()
        
root = Tk()
root.minsize(800, 400)
root.title('Converter by Xenorm')
root.configure(bg='deep sky blue')

from_lbl = Label(root, text='Click on the blank space', bg='deep sky blue', font='Comicsansms, 10')
from_lbl.pack()

exit_button = Button(root, text='Exit', fg='red', bg='black', font='freesansbold, 14', command=quit) 
exit_button.pack(side=BOTTOM)

cvt_from = StringVar()
cvt_to = StringVar()

def do_convert():
    feet_val = float(cvt_from.get())
    meters_val = feet_val * 0.3048
    cvt_to.set('%s meters' % meters_val)

from_lbl = Label(root, text='Enter FEET (numbers only):', bg='deep sky blue', fg='black', font='12')
from_lbl.pack() 

from_entry = Entry(root, bg='sky blue', fg='black', font='freesansbold, 14', textvariable=cvt_from) 
from_entry.pack()

to_lbl = Label(root, text='Result:', bg='sky blue', fg='black', font='comicsansms, 35')
to_lbl.pack() 

result_lbl = Label(root, textvariable=cvt_to, bg='sky blue', fg='black', font='comicsansms, 20')
result_lbl.pack()

convert_btn = Button(root, text='<CONVERT TO METERS>', bg='deep sky blue', fg='purple', font='comicsansms, 25', command=do_convert)
convert_btn.pack()


menubar = Menu(root) 
filemenu = Menu(menubar, tearoff=0) 
filemenu.add_command(label="New", command=myNew)
filemenu.add_command(label="Open", command=donothing) 
filemenu.add_command(label="Save", command=donothing) 
filemenu.add_command(label="Save as...", command=donothing) 
filemenu.add_command(label="Close", command=donothing)  
filemenu.add_separator()  
filemenu.add_command(label="Close", command=mQuit)
menubar.add_cascade(label="File", menu=filemenu) 
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="Undo", command=donothing)  
editmenu.add_separator()  
editmenu.add_command(label="Cut", command=donothing) 
editmenu.add_command(label="Copy", command=donothing) 
editmenu.add_command(label="Paste", command=donothing) 
editmenu.add_command(label="Delete", command=donothing) 
editmenu.add_command(label="Select All", command=donothing)  
menubar.add_cascade(label="Edit", menu=editmenu) 
helpmenu = Menu(menubar, tearoff=0) 
helpmenu.add_command(label="Help Index", command=donothing) 
helpmenu.add_command(label="About...", command=donothing) 
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar) 
root.mainloop() 
