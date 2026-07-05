from tkinter import *
import math

# Create window
root = Tk()
root.title("MATHEMATICAL CALCULATOR (MC)")
root.geometry("360x550")

# Display
e = Entry(root, font=("Arial", 24), justify="right", bd=8)
e.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

# Functions
def press(x):
    e.insert(END, x)

def clear():
    e.delete(0, END)

def equal():
    try:
        result = eval(e.get().replace("^", "**"))
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def square_root():
    try:
        result = math.sqrt(float(e.get()))
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def off():
    root.destroy()

# Make rows and columns expand
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Buttons
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),("%",4,1),("^",4,2),("+",4,3),
]

for text,row,col in buttons:
    Button(root,text=text,font=("Arial",18),
           command=lambda t=text:press(t)).grid(
           row=row,column=col,
           sticky="nsew",padx=4,pady=4)

Button(root,text="√",font=("Arial",18),
       command=square_root).grid(row=5,column=0,sticky="nsew",padx=4,pady=4)

Button(root,text="C",font=("Arial",18),
       command=clear).grid(row=5,column=1,sticky="nsew",padx=4,pady=4)

Button(root,text="=",font=("Arial",18),
       command=equal).grid(row=5,column=2,sticky="nsew",padx=4,pady=4)

Button(root,text="OFF",font=("Arial",18),
       bg="red",fg="white",
       command=off).grid(row=5,column=3,sticky="nsew",padx=4,pady=4)

root.mainloop()