import tkinter as tk

root = tk.Tk()
root.wm_title("Calculator exam")

# Definitions of your GUI elements and functions go here
ctrlframe = tk.Frame(root)
ctrlframe.pack(side=tk.LEFT, anchor = tk.NW)

number1 = 0
number2 = 0 
result = "0"
button = "0"

display = tk.StringVar(value=button)

def nothing():
    print("button not assigned")
    
def buttonNumber(button):
    display.set(button)
    
def add():
    number1 = int(Entry_Display.get())
    display.set(0)
 
def subtract():
    number1 = int(Entry_Display.get())
    display.set(0)
     
def equals():
    number2 = int(Entry_Display.get())
    result = number1 + number2
    display.set(result)
    
def clear():
    number1=0
    number2=0
    display.set("0")
      

Entry_Display = tk.Entry(ctrlframe, text=display, width = 20)
Entry_Display.grid(row=0,columnspan=4, sticky = "ew")

button_7 = tk.Button(ctrlframe, text = "7", command=buttonNumber("7"),width=5)  #creates button for aquiring data
button_7.grid(row=1, column=0)

button_8 = tk.Button(ctrlframe, text = "8", command=buttonNumber("8"),width=5)  #creates button for aquiring data
button_8.grid(row=1, column=1)

button_9 = tk.Button(ctrlframe, text = "9", command=buttonNumber("9"),width=5)  #creates button for aquiring data
button_9.grid(row=1, column=2)

button_clear = tk.Button(ctrlframe, text = "C", command=clear,width=5)  #creates button for aquiring data
button_clear.grid(row=1, column=3)

button_4 = tk.Button(ctrlframe, text = "4", command=buttonNumber("4"),width=5)  #creates button for aquiring data
button_4.grid(row=2, column=0)

button_5 = tk.Button(ctrlframe, text = "5", command=buttonNumber("5"),width=5)  #creates button for aquiring data
button_5.grid(row=2, column=1)

button_6 = tk.Button(ctrlframe, text = "6", command=buttonNumber("6"),width=5)  #creates button for aquiring data
button_6.grid(row=2, column=2)

button_minus = tk.Button(ctrlframe, text = "-", command=subtract,width=5)  #creates button for aquiring data
button_minus.grid(row=2, column=3)

button_1 = tk.Button(ctrlframe, text = "1", command=buttonNumber("1"),width=5)  #creates button for aquiring data
button_1.grid(row=3, column=0)

button_2 = tk.Button(ctrlframe, text = "2", command=buttonNumber("2"),width=5)  #creates button for aquiring data
button_2.grid(row=3, column=1)

button_3 = tk.Button(ctrlframe, text = "3", command=buttonNumber("3"),width=5)  #creates button for aquiring data
button_3.grid(row=3, column=2)

button_plus = tk.Button(ctrlframe, text = "+", command=add,width=5)  #creates button for aquiring data
button_plus.grid(row=3, column=3)

button_0 = tk.Button(ctrlframe, text = "0", command=buttonNumber(0),width=5)  #creates button for aquiring data
button_0.grid(row=4, column=0)

button_decimal = tk.Button(ctrlframe, text = ".", command=nothing,width=5)  #creates button for aquiring data
button_decimal.grid(row=4, column=1)

button_negative = tk.Button(ctrlframe, text = "(-)", command=nothing,width=5)  #creates button for aquiring data
button_negative.grid(row=4, column=2)

button_equals = tk.Button(ctrlframe, text = "=", command=equals,width=5)  #creates button for aquiring data
button_equals.grid(row=4, column=3)



tk.mainloop()

