import tkinter as tk

root = tk.Tk()
root.wm_title("Calculator exam")


padding  = 2
widthOfButton = 5
ansClear = 0

def answerClear():
    global ansClear
    if ansClear == 1:
        clear()
        ansClear = 0

def key_press1():
    answerClear()
    label_display['text'] += "1"
    
def key_press2():
    answerClear()
    label_display['text'] += "2"
    
def key_press3():
    answerClear()
    label_display['text'] += "3"
    
def key_press4():
    answerClear()
    label_display['text'] += "4"
    
def key_press5():
    answerClear()
    label_display['text'] += "5"
    
def key_press6():
    answerClear()
    label_display['text'] += "6"
    
def key_press7():
    answerClear()
    label_display['text'] += "7"
    
def key_press8():
    answerClear()
    label_display['text'] += "8"
    
def key_press9():
    answerClear()
    label_display['text'] += "9"
    
def key_press0():
    answerClear()
    label_display['text'] += "0"
    
    
def clear():
    label_display['text'] = ""
    
def add():
    answerClear()
    label = label_display['text']

    if label[len(label)-2] == "+":
        return
    if label[len(label)-2] == "-":
        label = label[0:len(label)-3]
        label_display['text'] = label
        
    label_display['text'] += " + "
    
def subtract():
    answerClear()
    label = label_display['text']
    
    if label[len(label)-2] == "-":
        return
    if label[len(label)-2] == "+":
        label = label[0:len(label)-3]
        label_display['text'] = label
        
    label_display['text'] += " - "
    
def calculate():
    global ansClear
    answerClear()
    answer = 0.0
    stringCalc = str.split(label_display['text'])
    if len(stringCalc) <= 2:
        label_display['text'] += "Error invalid input"
        return
    if stringCalc[0] == " ":
        label_display['text'] += "Error invalid input"
        return
    if len(stringCalc) > 3:
        label_display['text'] += "Error invalid input"
        return
    
    if stringCalc[1] == "+":
        answer = float(stringCalc[0]) + float(stringCalc[2])
        label_display['text'] = str(answer)
        
    if stringCalc[1] == "-":
        answer = float(stringCalc[0]) - float(stringCalc[2])
        label_display['text'] = str(answer)
    ansClear = 1

label_display = tk.Label(root, text="")

label_display.grid(row=0, columnspan = 3, column=0, padx=(5,5), pady=(10,10))

button_1 = tk.Button(root, text="1", width=widthOfButton, command = key_press1)
button_2 = tk.Button(root, text="2", width=widthOfButton, command = key_press2)
button_3 = tk.Button(root, text="3", width=widthOfButton, command = key_press3)
clear_button = tk.Button(root, text="CE", width=widthOfButton, command = clear)

button_4 = tk.Button(root, text="4", width=widthOfButton, command = key_press4)
button_5 = tk.Button(root, text="5", width=widthOfButton, command = key_press5)
button_6 = tk.Button(root, text="6", width=widthOfButton, command = key_press6)
addition_button = tk.Button(root, text="+", width=widthOfButton, command = add)

button_7 = tk.Button(root, text="7", width=widthOfButton, command = key_press7)
button_8 = tk.Button(root, text="8", width=widthOfButton, command = key_press8)
button_9 = tk.Button(root, text="9", width=widthOfButton, command = key_press9)
subtract_button = tk.Button(root, text="-", width=widthOfButton, command = subtract)

plus_negative_button = tk.Button(root, text="+/-", width=widthOfButton)
button_0 = tk.Button(root, text="0", width=widthOfButton, command = key_press0)
decimal_button = tk.Button(root, text=".", width=widthOfButton)
equals_button = tk.Button(root, text="=", width=widthOfButton, command = calculate)


button_1.grid(row=1, column=0, pady=(padding, padding), padx=(padding, padding))
button_2.grid(row=1, column=1, pady=(padding, padding), padx=(padding, padding))
button_3.grid(row=1, column=2, pady=(padding, padding), padx=(padding, padding))
clear_button.grid(row=1, column=3, pady=(padding, padding), padx=(padding, padding))

button_4.grid(row=2, column=0, pady=(padding, padding), padx=(padding, padding))
button_5.grid(row=2, column=1, pady=(padding, padding), padx=(padding, padding))
button_6.grid(row=2, column=2, pady=(padding, padding), padx=(padding, padding))
addition_button.grid(row=2, column=3, pady=(padding, padding), padx=(padding, padding))

button_7.grid(row=3, column=0, pady=(padding, padding), padx=(padding, padding))
button_8.grid(row=3, column=1, pady=(padding, padding), padx=(padding, padding))
button_9.grid(row=3, column=2, pady=(padding, padding), padx=(padding, padding))
subtract_button.grid(row=3, column=3, pady=(padding, padding), padx=(padding, padding))

#plus_negative_button.grid(row=4, column=0, pady=(padding, padding), padx=(padding, padding))
button_0.grid(row=4, column=1, pady=(padding, padding), padx=(padding, padding))
#decimal_button.grid(row=4, column=2, pady=(padding, padding), padx=(padding, padding))
equals_button.grid(row=4, column=3, pady=(padding, padding), padx=(padding, padding))

# Definitions of your GUI elements and functions go here

tk.mainloop()
