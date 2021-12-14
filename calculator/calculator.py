import tkinter as tk

root = tk.Tk()
root.wm_title("Calculator exam")

# Definitions of your GUI elements and functions go here
# functions for calling
# add to a running sum until clear and create variables
var_num = tk.StringVar(value="0.0")
var_sol = tk.StringVar(value="0.0")

runningsum = 0.0
add = 0
sub = 0 
div = 0
mult = 0

def Add():
    global runningsum
    global add
    global sub
    global div
    global mult
    num = float(var_num.get())
    runningsum = num
    add = 1
    sub = 0 
    div = 0
    mult = 0
    
def Sub():
    global runningsum
    global add
    global sub
    global div
    global mult
    num = float(var_num.get())
    runningsum = num
    add = 0
    sub = 1 
    div = 0
    mult = 0
    
def Div():
    global runningsum
    global add
    global sub
    global div
    global mult
    num = float(var_num.get())
    runningsum = num
    add = 0
    sub = 0 
    div = 1
    mult = 0
    
def Mult():
    global runningsum
    global add
    global sub
    global div
    global mult
    num = float(var_num.get())
    runningsum = num
    add = 0
    sub = 0 
    div = 0
    mult = 1
    
def Clear():
    global runningsum
    global add
    global sub
    global div
    global mult
    runningsum = 0.0
    var_sol.set(runningsum) 
    add = 0
    sub = 0 
    div = 0
    mult = 0

def Calc():
    global runningsum
    global add
    global sub
    global div
    global mult
    num = float(var_num.get()) 
    if (add == 1): 
        runningsum += num
    elif (sub == 1):
        runningsum -= num
    elif (div == 1): 
        runningsum = runningsum/num
    elif (mult == 1): 
        runningsum *= num
    else:
        print("Error!")
    var_sol.set(runningsum)
    
# entry windows
label_num = tk.Label(root,text = "Enter Numbers:", width=15)
label_sol = tk.Label(root,text = "Solution:", width=15)


label_add = tk.Button(root,text = "+", width=10, command = Add)
label_sub = tk.Button(root,text = "-", width=10, command = Sub)
label_div = tk.Button(root,text = "/", width=10, command = Div)
label_mult = tk.Button(root,text = "x", width=10, command = Mult)
label_clear = tk.Button(root,text = "C", width=10, command = Clear)
label_calc = tk.Button(root,text = "=", width=10, command = Calc)


entry_num = tk.Entry(root, textvariable=var_num, width=15)
entry_sol = tk.Entry(root, textvariable=var_sol, width=15)

entry_num.grid(row=0,column=1)
entry_sol.grid(row=1,column=1)

label_num.grid(row=0,column=0)
label_sol.grid(row=1,column=0)
label_add.grid(row=2,column=0)
label_sub.grid(row=2,column=1)
label_div.grid(row=2,column=2)
label_mult.grid(row=3,column=0)
label_clear.grid(row=3,column=1)
label_calc.grid(row=3,column=2)


tk.mainloop()
