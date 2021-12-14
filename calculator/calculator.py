# by MICHAEL YAKOVLEV

import tkinter as tk

root = tk.Tk()
root.wm_title("Calculator exam")

# Definitions of your GUI elements and functions go here

    
def b1():
    #obtains current displays
    stringy=str(equation.get())
    #adds new symbol
    stringy=stringy+"1"
    #updates display
    equation.set("{:}".format(stringy))
def b2():
    stringy=str(equation.get())
    stringy=stringy+"2"
    equation.set("{:}".format(stringy))  
def b3():
    stringy=str(equation.get())
    stringy=stringy+"3"
    equation.set("{:}".format(stringy))
def b4():
    stringy=str(equation.get())
    stringy=stringy+"4"
    equation.set("{:}".format(stringy))   
def b5():
    stringy=str(equation.get())
    stringy=stringy+"5"
    equation.set("{:}".format(stringy))
def b6():
    stringy=str(equation.get())
    stringy=stringy+"6"
    equation.set("{:}".format(stringy))    
def b7():
    stringy=str(equation.get())
    stringy=stringy+"7"
    equation.set("{:}".format(stringy))
def b8():
    stringy=str(equation.get())
    stringy=stringy+"8"
    equation.set("{:}".format(stringy))    
def b9():
    stringy=str(equation.get())
    stringy=stringy+"9"
    equation.set("{:}".format(stringy))    
def b0():
    stringy=str(equation.get())
    stringy=stringy+"0"
    equation.set("{:}".format(stringy))    
def bp():
    stringy=str(equation.get())
    stringy=stringy+"+"
    equation.set("{:}".format(stringy))    
def bm():
    stringy=str(equation.get())
    stringy=stringy+"-"
    equation.set("{:}".format(stringy))   

# by MICHAEL YAKOVLEV

def beq():
    #obtains current displays
    stringy=str(equation.get())
    #if equationstarts with a sign, it will skip it for figuring out terms and will apply later
    if stringy[0]=="-" or stringy[0]=="+":
        i=1
        idd=0
        #finds ID of the operation sign
        while (i<len(stringy)):
            if stringy[i]=="+" or stringy[i]=="-":
                idd=i
            i=i+1
        val_1=""
        val_2=""
        i=1
        #composes the string for the first number
        while (i<idd):
            val_1=val_1+stringy[i]
            i=i+1
        i=idd+1
        #composes the string for the second number
        while (i<len(stringy)):
            val_2=val_2+stringy[i]
            i=i+1
        answer=0
        #if first number is negative, multiply by -1
        #calculates answer by turning string numbers into integers
        #performs calculation if only there is operation on two numbers, otherwise skips
        if stringy[0]=="-" and idd!=0:
            if stringy[idd]=="+":
                answer=-1*int(val_1)+int(val_2)
            if stringy[idd]=="-":
                answer=-1*int(val_1)-int(val_2)
        if stringy[0]=="+" and idd!=0:
            if stringy[idd]=="+":
                answer=int(val_1)+int(val_2)
            if stringy[idd]=="-":
                answer=int(val_1)-int(val_2)
    #if equationstarts with a number, proceed normally
    else:
        i=0
        idd=0
        #finds ID of the operation sign
        while (i<len(stringy)):
            if stringy[i]=="+" or stringy[i]=="-":
                idd=i
            i=i+1
        val_1=""
        val_2=""
        i=0
        #composes the string for the first number
        while (i<idd):
            val_1=val_1+stringy[i]
            i=i+1
        i=idd+1
        #composes the string for the second number
        while (i<len(stringy)):
            val_2=val_2+stringy[i]
            i=i+1
        answer=0
        #calculates answer by turning string numbers into integers
        if stringy[idd]=="+":
            answer=int(val_1)+int(val_2)
        if stringy[idd]=="-":
            answer=int(val_1)-int(val_2)
    #in case there is no operator, number=number
    if idd==0:
        stringy=stringy+"="+stringy
    #otherwise => add the answer value to display
    else:
        stringy=stringy+"="+str(answer)
    #updates display to include the answer
    equation.set("{:}".format(stringy))
    
# by MICHAEL YAKOVLEV

def cl():
    #clears the display
    equation.set("{:}".format(""))   

#UI setup
equation= tk.StringVar("")
display = tk.Label(root,font=66,textvariable=equation)
_button1=tk.Button(root,text="1",font=66,fg="blue",command= b1)
_button2=tk.Button(root,text="2",font=66,fg="blue",command= b2)
_button3=tk.Button(root,text="3",font=66,fg="blue",command= b3)
_button4=tk.Button(root,text="4",font=66,fg="blue",command= b4)
_button5=tk.Button(root,text="5",font=66,fg="blue",command= b5)
_button6=tk.Button(root,text="6",font=66,fg="blue",command= b6)
_button7=tk.Button(root,text="7",font=66,fg="blue",command= b7)
_button8=tk.Button(root,text="8",font=66,fg="blue",command= b8)
_button9=tk.Button(root,text="9",font=66,fg="blue",command= b9)
_button0=tk.Button(root,text="0",font=66,fg="blue",command= b0)
p_button=tk.Button(root,text="+",font=222,command= bp)
m_button=tk.Button(root,text="-",font=222,command= bm)
eq_button=tk.Button(root,text="=",font=222,command= beq)
cl_button=tk.Button(root,text="CLEAR",font=66,fg="green",command= cl)
quit_button=tk.Button(root,text="Quit",fg="red",font=66,command= quit)

# by MICHAEL YAKOVLEV

#grid setup
display.grid(row=0,column=0,columnspan=3,padx=(5,0),pady=(5,5))
_button1.grid(row=1,column=1,pady=(0,5))
_button2.grid(row=1,column=2,pady=(0,5))
_button3.grid(row=1,column=3,pady=(0,5))
_button4.grid(row=2,column=1,pady=(0,5))
_button5.grid(row=2,column=2,pady=(0,5))
_button6.grid(row=2,column=3,pady=(0,5))
_button7.grid(row=3,column=1,pady=(0,5))
_button8.grid(row=3,column=2,pady=(0,5))
_button9.grid(row=3,column=3,pady=(0,5))
_button0.grid(row=4,column=2,pady=(0,5))
p_button.grid(row=5,column=1,columnspan=3,pady=(15,5))
m_button.grid(row=6,column=1,columnspan=3,pady=(0,5))
eq_button.grid(row=7,column=1,columnspan=3,pady=(0,5))
cl_button.grid(row=8,column=1,columnspan=3,pady=(15,5))
quit_button.grid(row=9,column=1,columnspan=3,pady=(25,5))
tk.mainloop()

# by MICHAEL YAKOVLEV