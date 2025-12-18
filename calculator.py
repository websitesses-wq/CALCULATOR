"""
Python GUI Calculator
Built using Tkinter
"""

from tkinter import *

# Create window
window = Tk()
window.title("Python Calculator")
window.geometry("350x500")
window.config(bg="black")

# Display
display = Entry(
    window,
    font=("Arial", 22),
    bg="#2b1d0e",
    fg="gold",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=15, padx=10, pady=20)

# Functions
def insert_value(value):
    display.insert(END, value)

def clear_display():
    display.delete(0, END)

def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(END, result)
    except:
        clear_display()
        display.insert(END, "Error")

def square():
    value = float(display.get())
    clear_display()
    display.insert(END, value ** 2)

def cube():
    value = float(display.get())
    clear_display()
    display.insert(END, value ** 3)

# Button style
btn_style = {
    "font": ("Arial", 14),
    "bg": "#5c3a1e",
    "fg": "white",
    "width": 6,
    "height": 2
}

# Buttons
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("+",4,2), ("=",4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        Button(window, text=text, command=calculate, **btn_style).grid(row=row, column=col)
    else:
        Button(window, text=text, command=lambda t=text: insert_value(t), **btn_style).grid(row=row, column=col)

# Extra buttons
Button(window, text="C", command=clear_display, **btn_style).grid(row=5, column=0)
Button(window, text="x²", command=square, **btn_style).grid(row=5, column=1)
Button(window, text="x³", command=cube, **btn_style).grid(row=5, column=2)
Button(window, text="xʸ", command=lambda: insert_value("**"), **btn_style).grid(row=5, column=3)

window.mainloop()
