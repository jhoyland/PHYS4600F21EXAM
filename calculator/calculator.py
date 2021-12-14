import tkinter as tk
import numpy as np
import math



expression = "" # 1+1

def button_press(num):
    global expression
    expression = expression + str(num) #expression variable stores the entered elements one after another.
    var_eq.set(expression) #sets the tk varibale as the expression
    return


def calculate():
    global expression
    result = str(eval(expression))  #python built in evaluate function.
    var_eq.set(result)
    return    
    
def clear():
    global expression
    expression = ""
    var_eq.set(expression) #empty the box
    return
    
root = tk.Tk()
root.wm_title("Calculator exam")

ctrlframe = tk.Frame(root)
ctrlframe.pack(side=tk.LEFT)


# Definitions of your GUI elements and functions go here

label_display = tk.Label(ctrlframe,text="display",width=20)
var_eq = tk.StringVar(value="")
entry_display = tk.Entry(ctrlframe,text="display",textvariable=var_eq,width=20)
entry_display.grid(row=0, column=1,padx=(0,10),pady=(0,10))

#needed lambda python function for button presses to work.
num1_button = tk.Button(ctrlframe,text="1",command = lambda: button_press(1))
num1_button.grid(row=2,column=0,columnspan=1)

num2_button = tk.Button(ctrlframe,text="2",command = lambda: button_press(2))
num2_button.grid(row=2,column=1,columnspan=1)

num3_button = tk.Button(ctrlframe,text="3",command = lambda: button_press(3))
num3_button.grid(row=2,column=2,columnspan=1)

num4_button = tk.Button(ctrlframe,text="4",command = lambda: button_press(4))
num4_button.grid(row=3,column=0,columnspan=1)

num5_button = tk.Button(ctrlframe,text="5",command = lambda: button_press(5))
num5_button.grid(row=3,column=1,columnspan=1)

num6_button = tk.Button(ctrlframe,text="6",command = lambda: button_press(6))
num6_button.grid(row=3,column=2,columnspan=1)

num7_button = tk.Button(ctrlframe,text="7",command = lambda: button_press(7))
num7_button.grid(row=4,column=0,columnspan=1)

num8_button = tk.Button(ctrlframe,text="8",command = lambda: button_press(8))
num8_button.grid(row=4,column=1,columnspan=1)

num9_button = tk.Button(ctrlframe,text="9",command = lambda: button_press(9))
num9_button.grid(row=4,column=2,columnspan=1)

num0_button = tk.Button(ctrlframe,text="0",command = lambda: button_press(0))
num0_button.grid(row=5,column=1,columnspan=1)


add_button = tk.Button(ctrlframe,text="+",command= lambda: button_press("+"))
add_button.grid(row=6,column=1,columnspan=2)

subtract_button = tk.Button(ctrlframe,text="-",command= lambda: button_press("-"))
subtract_button.grid(row=7,column=1,columnspan=2)

equal_button = tk.Button(ctrlframe,text="=",command=calculate)
equal_button.grid(row=8,column=1,columnspan=2)

clear_button = tk.Button(ctrlframe,text="clear",command=clear)
clear_button.grid(row=9,column=1,columnspan=2)




tk.mainloop()
