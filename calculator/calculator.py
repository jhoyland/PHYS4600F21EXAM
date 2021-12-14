import tkinter as tk

root = tk.Tk()
root.wm_title("Calculator exam")

# Definitions of your GUI elements and functions go here


ctrlframe = tk.Frame(root)
ctrlframe.pack(side=tk.LEFT)

name = tk.Label(ctrlframe, text="Calculator",width=15)
name.grid(row=0,column=1,columnspan=3,padx=(0,10))
var_A = tk.StringVar(value="0")
entry_A = tk.Entry(ctrlframe, textvariable=var_A, width=15)


def on_click(var_A):
   entry.insert(0,var_A)

entry=tk.Entry(ctrlframe, width= 20)
entry.grid(row=1,column=1,columnspan=3,padx=(0,10))


se = tk.StringVar(value="7")
seven = tk.Button(ctrlframe,text="7",command=lambda:on_click("7"))
seven.grid(row=3,column=1,columnspan=1,sticky="ew")
eight = tk.Button(ctrlframe,text="8",command=lambda:on_click("8"))
eight.grid(row=3,column=2,columnspan=1,sticky="ew")
nine = tk.Button(ctrlframe,text="9",command=lambda:on_click("9"))
nine.grid(row=3,column=3,columnspan=1,sticky="ew")
four = tk.Button(ctrlframe,text="4",command=lambda:on_click("4"))
four.grid(row=4,column=1,columnspan=1,sticky="ew")
five = tk.Button(ctrlframe,text="5",command=lambda:on_click("5"))
five.grid(row=4,column=2,columnspan=1,sticky="ew")
six = tk.Button(ctrlframe,text="6",command=lambda:on_click("6"))
six.grid(row=4,column=3,columnspan=1,sticky="ew")
one = tk.Button(ctrlframe,text="1",command=lambda:on_click("1"))
one.grid(row=5,column=1,columnspan=1,sticky="ew")
two = tk.Button(ctrlframe,text="2",command=lambda:on_click("2"))
two.grid(row=5,column=2,columnspan=1,sticky="ew")
three = tk.Button(ctrlframe,text="3",command=lambda:on_click("3"))
three.grid(row=5,column=3,columnspan=1,sticky="ew")


def calc():
    add=var_A+var_A
    entry.insert(0,add)
    #calculation
def add():
    3+4
def sub():
    3+3
    
calc_button = tk.Button(ctrlframe,text="=",command=lambda:on_click("="))
calc_button.grid(row=6,column=3,columnspan=1,sticky="ew")
calc_button = tk.Button(ctrlframe,text="+",command=lambda:on_click("+"))
calc_button.grid(row=6,column=2,columnspan=1,sticky="ew")
calc_button = tk.Button(ctrlframe,text="-",command=lambda:on_click("-"))
calc_button.grid(row=6,column=1,columnspan=1,sticky="ew")

tk.mainloop()
