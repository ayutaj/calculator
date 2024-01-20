from tkinter import *
from tkinter import ttk

root = Tk(screenName="Calculator")
root.geometry("265x350")
frm = ttk.Frame(root, padding=30).grid()

#Initialize a Label to display the User Input
name=Label(frm, text="CALCULATOR", font=("Courier 18 bold"))
name.grid(row=0,column=0,columnspan=4,pady=5)

display=""
num1=""
num2=""
currop=""
flag=0
dotflag=0
ipnutlabel= Label(frm,text="", width=25,  borderwidth=3, relief="ridge",font=("Courier 12 bold"))
ipnutlabel.grid(columnspan=4,pady=10,ipady=10)

def backspace():
    global num1,num2,display,currop
    if(num1=="" and num2==""):
        display=""
    if(currop==''):
        if len(num1)>0:
            num1=num1[0:-1]
    else:
        if len(num2)>0:    
            num2=num2[0:-1]
    if(len(display)>0):
        display=display[0:-1]
    ipnutlabel['text']=display

def onclick(number):
    global display,num1,num2,flag
    if flag==0:
        display=""
        flag=1
    display= display+number
    if currop=="":
        num1=num1+number
    else:
        num2=num2+number
    ipnutlabel["text"]=display
    
def ondot():
    global display,dotflag,num1,num2,flag
    if(dotflag==0 and( (display=="" and flag==0) or flag==1)):
        dotflag=1
        flag=1
        if currop=="":
            num1=num1+"."
        else:
            num2+="."
        display+='.'
    else:
        display=""
    ipnutlabel["text"]=display
def operatorhandler(op):
    global currop,num1,num2, display,dotflag
    if(num1=='.' or num2=="."):
        return
    dotflag=0
    if num1=='' and num2=="":
        display=""
        ipnutlabel["text"]=display
        pass
    elif op=="+" or op=="-" or op=="*" or op=="/" or op=="%":
        currop=op
        display=""
    elif op=="C":
        num1="0"
        num2=""
        currop=""
        display=""
    elif op=="CE":
        num2=""
        if currop=="":
            num1=""
        display=""    
    elif op=="cut":
        if currop=="":
            if len(num1)>0:
                num1=num1[0:-1]
        else:
            if len(num2>0):
                num2=num2[0:-1]
    ipnutlabel["text"]=display

def handlingequal():
    global display,flag,num1,num2,currop,dotflag
    dotflag=0
    if num1!="" and num2=="":
        ipnutlabel["text"]=display
    elif(num1==""):
        pass
    else:
        val1=float(num1)
        val2=float(num2)  
        f=0  
        if currop=="+":
            ans=val1+val2
        elif currop=='-':
            ans=val1-val2
        elif currop=='*':
            ans=val1*val2
        elif currop=='%':
            ans=val2/100
        elif currop=='/':
            if(val2!=0):
                ans=val1/val2
            else:
                f=1
                ans="divide by zero error"
        if(f==0):
            display=str(ans)
        else:
            display=ans
        flag=0
        currop=""
        num1=""
        num2=""
        ipnutlabel["text"]=display
    
    
    # Changing position of cursor one character right 

BUttonpercentage=Button(frm,text="%",padx="23",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("As")).grid(row=2,column=0,padx=0,pady=2)
ButtonCE=Button(frm,text="CE",padx="22",pady="10", borderwidth=1, relief="raised",command=lambda :operatorhandler("CE")).grid(row=2,column=1,padx=0,pady=2)
ButtonC=Button(frm,text="C",padx="23",pady="10", borderwidth=1, relief="raised",command=lambda : operatorhandler("C")).grid(row=2,column=2,padx=0,pady=2)
Buttoncut=Button(frm,text="<x]",padx="20",pady="10", borderwidth=1, relief="raised",command=lambda : backspace()).grid(row=2,column=3,padx=0,pady=2)

Button7=Button(frm,text="7",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("7")).grid(row=3,column=0,padx=0,pady=2)
Button8=Button(frm,text="8",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("8")).grid(row=3,column=1,padx=0,pady=2)
Button9=Button(frm,text="9",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("9")).grid(row=3,column=2,padx=0,pady=2)
Buttonmultiply=Button(frm,text="x",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : operatorhandler("*")).grid(row=3,column=3,padx=0,pady=2)

Button4=Button(frm,text="4",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("4")).grid(row=4,column=0,padx=0,pady=2)
Button5=Button(frm,text="5",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("5")).grid(row=4,column=1,padx=0,pady=2)
Button6=Button(frm,text="6",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("6")).grid(row=4,column=2,padx=0,pady=2)
Buttonsub=Button(frm,text="-",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : operatorhandler("-")).grid(row=4,column=3,padx=0,pady=2)

Button1=Button(frm,text="1",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("1")).grid(row=5,column=0,padx=0,pady=2)
Button2=Button(frm,text="2",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("2")).grid(row=5,column=1,padx=0,pady=2)
Button3=Button(frm,text="3",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("3")).grid(row=5,column=2,padx=0,pady=2)
Buttonadd=Button(frm,text="+",padx="23",pady="10", borderwidth=1, relief="raised",command=lambda : operatorhandler("+")).grid(row=5,column=3,padx=0,pady=2)


Button0=Button(frm,text="0",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : onclick("0")).grid(row=6,column=0,padx=0,pady=2)
Buttondot=Button(frm,text=".",padx="26",pady="10", borderwidth=1, relief="raised",command=lambda : ondot()).grid(row=6,column=1,padx=0,pady=2)
Buttondivide=Button(frm,text="/",padx="25",pady="10", borderwidth=1, relief="raised",command=lambda : operatorhandler("/")).grid(row=6,column=2,padx=0,pady=2)
Buttonequal=Button(frm,text="=",padx="23",pady="10", borderwidth=1, relief="raised",command=lambda : handlingequal()).grid(row=6,column=3,padx=0,pady=2)



root.mainloop()