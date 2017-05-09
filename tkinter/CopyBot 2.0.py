import sys
from tkinter import *


def mHello():
    mText=ment.get()
    mlabel1 = Label(myApp,text=mText).pack()

def myNew():
    mlabel1 = Label(myApp,text="JUST A JOKE!!!").pack()

def myOpen():
    myOpen = askopenfilename()
    mlabel4 = Label(myApp,text=myOpen).pack()

def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = tkMessageBox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        myApp.destroy()
        
    
myApp = Tk()
#create a string variable
ment = StringVar()

#set the size of window
myApp.minsize(800, 400)

myApp.title('COPYBOT 2.0 By Xenorm')
myApp.configure(bg='sky blue')

mLabel = Label(myApp, bg='sky blue', fg='black', text='Write Anything', font='freesansbold, 14').pack()

mButton = Button(myApp, bg='sky blue', fg='black', text ='DONE', font='freesansbold, 10', command = mHello).pack()

#set the ment variable from the text entry box
mEntry = Entry(myApp, bg='sky blue', fg='black', font='freesansbold, 14', textvariable=ment).pack()

#create the menubar
menubar = Menu(myApp)

#create the file component of that menubar
filemenu = Menu(menubar, tearoff=0)

#Add the sub headings to the file menu
filemenu.add_command(label="New", command=myNew)
filemenu.add_command(label="Open", command=myOpen)
filemenu.add_command(label="Save As...")
filemenu.add_command(label="Close", command=mQuit)

menubar.add_cascade(label="File",menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help docs")
helpmenu.add_command(label="About",command=mAbout)
menubar.add_cascade(label="Help",menu=helpmenu)



#add menubar to the window
myApp.config(menu=menubar)

myApp.mainloop()
