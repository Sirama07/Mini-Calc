from tkinter import *
root=Tk()
root.title("SIMPLE CALCULATOR")
e=Entry(root,width=60,borderwidth=3)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=20)

def clicks(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))
def clear():
    e.delete(0,END)

def add():
    a=e.get()
    global x
    global choose
    choose="ADD"
    x=int(a)
    e.delete(0,END)
def sub():
    a = e.get()
    global x
    global choose
    choose = "SUB"
    x = int(a)
    e.delete(0, END)
def mul():
    a = e.get()
    global x
    global choose
    choose = "MULT"
    x = int(a)
    e.delete(0, END)
def divv():
    a = e.get()
    global x
    global choose
    choose = "DIV"
    x = int(a)
    e.delete(0, END)
def equall():
    aa=e.get()
    e.delete(0,END)
    if choose=="ADD":
        e.insert(0,x+int(aa))
    elif choose=="SUB":
        e.insert(0,x-int(aa))
    elif choose=="MULT":
        e.insert(0,x*int(aa))
    if choose=="DIV":
        e.insert(0,x/int(aa))

button1=Button(root,text="1",padx=40,pady=20,command=lambda:clicks(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:clicks(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:clicks(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:clicks(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:clicks(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:clicks(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:clicks(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:clicks(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:clicks(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:clicks(0))

buttonEqual=Button(root,text="=",padx=40,pady=20,command=equall)
buttonClear=Button(root,text="CLEAR",padx=25,pady=19,command=clear)

buttonAdd=Button(root,text="+",padx=40,pady=20,command=add)
buttonSub=Button(root,text="-",padx=40,pady=20,command=sub)
buttonMult=Button(root,text="*",padx=40,pady=20,command=mul)
buttonDiv=Button(root,text="/",padx=40,pady=20,command=divv)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=2)
button5.grid(row=2,column=0)
button6.grid(row=2,column=1)
button7.grid(row=1,column=1)
button8.grid(row=1,column=2)
button9.grid(row=1,column=0)
button0.grid(row=4,column=1)
buttonEqual.grid(row=4,column=0)
buttonClear.grid(row=4,column=2)
buttonAdd.grid(row=4,column=3)
buttonSub.grid(row=3,column=3)
buttonMult.grid(row=2,column=3)
buttonDiv.grid(row=1,column=3)
root.mainloop()
