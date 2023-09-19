from tkinter.ttk import *
from tkinter import *
from time import *

colorlabel = "white"
root = Tk()
root['bg'] = 'black'
root.title("Settings")
x = IntVar()

def get():
    global colorlabel
    global x
    validity = x.get()
    if validity == 1:
        validity = "You saved changes"
    elif validity == 0:
        validity = "You did not save changes"
    num = StringVar()
    volume = horizontal.get()
    brightness = horizontal2.get()
    bar = Progressbar(root,orient="horizontal",length=280)
    bar.grid(row=8,column=0,columnspan=2)
    percent = Label(root,textvariable=num,font=('Helvetica',10),bg="black",fg="white")
    percent.grid(row=9,column=0,columnspan=2)
    end = Label(root,text="Close the window and read the shell",font=('Helvetica',10),bg="black",fg="white")
    #row is subject to change
    current = 0
    ceiling = 100
    while current<ceiling:
        import time
        time.sleep(0.05)
        bar['value']+=1
        current+=1
        num.set(str(current)+"%")
        root.update_idletasks()
    
    end.grid(row=10,column=0,columnspan=2)
    print("You set the volume to",volume)
    print("You set the brightness to",brightness)
    print("Your theme color is",colorlabel)
    print(validity)

def colorchange():
    global color
    global colorlabel
    color.destroy()
    if colorlabel == "white":
        color = Button(root,text="                               ",bg="red",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "red"
    elif colorlabel == "red":
        color = Button(root,text="                               ",bg="green",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "green"
    elif colorlabel == "green":
        color = Button(root,text="                               ",bg="blue",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "blue"
    elif colorlabel == "blue":
        color = Button(root,text="                               ",bg="yellow",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "yellow"
    elif colorlabel == "yellow":
        color = Button(root,text="                               ",bg="orange",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "orange"
    elif colorlabel == "orange":
        color = Button(root,text="                               ",bg="white",command=colorchange)
        color.grid(row=3,column=1)
        colorlabel = "white"

def updatetime():
    result = strftime("%I:%M:%S %p")
    ctime.config(text=result)

    root.after(1000,updatetime)

    
main = Label(root,text="SETTINGS",font=('Helvetica',30,'bold'),bg="black",fg="white",padx=10,pady=10)
main.grid(row=0,column=0,columnspan=2)

slider = Label(root,text="Volume",font=('Helvetica',14),bg="black",fg="white",padx=10,pady=10)
slider.grid(row=1,column=0)
horizontal = Scale(root,from_=0,to=100,orient=HORIZONTAL,bg='white')
horizontal.grid(row=1,column=1)
slider2 = Label(root,text="Brightness",font=('Helvetica',14),bg="black",fg="white",padx=10,pady=10)
slider2.grid(row=2,column=0)
horizontal2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,bg='white')
horizontal2.grid(row=2,column=1)
theme = Label(root,text="Color Theme",font=('Helvetica',14),bg="black",fg="white",padx=10,pady=10)
ins = Label(root,text="Click the box to change color",font=('Helvetica',10),bg="black",fg="white")
color = Button(root,text="                               ",bg="white",command=colorchange)
theme.grid(row=3,column=0)
color.grid(row=3,column=1)
ins.grid(row=4,column=0,columnspan=2)
savechanges = Checkbutton(root,text="Save changes",font=('Helvetica',14),variable=x,bg="white",fg="black",onvalue=1,offvalue=2)
savechanges.grid(row=5,column=0,columnspan=2)
ctime = Label(root,font=('Helvetica',14),bg="black",fg="white")
ctime.grid(row=6,column=0,columnspan=2)

updatetime()

submit = Button(root,text="Confirm",font=('Helvetica',14),bg='white',width=25,command=get)
#row is subject to change
submit.grid(row=7,column=0,columnspan=2)
root.mainloop()
