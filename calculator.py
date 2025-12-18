"""
Python GUI Calculator
Built using Tkinter
"""

from tkinter import * #Bring all Tkinter tools into this file

# Create window
window = Tk() # Creates a blank window
window.title("Python Calculator") # Sets the title (top bar text).
window.geometry("350x500") # Sets window width = 350 px, height = 500 px
window.config(bg="black") # Sets background color to black

# Display
display = Entry( # Entry - one-line text box
    window, # window - placed inside main window
    font=("Arial", 22), # font - text style and size
    bg="#2b1d0e", # bg - background color (golden-brown)
    fg="gold", # fg - text color (gold)
    justify="right" # justify="right" - numbers align right (like real calculator)
)
display.grid(row=0, # row=0 - first row
             column=0, # column=0 - first column
             columnspan=4,  # columnspan=4 - spans across 4 columns
             ipadx=10,  #ipadx/ipady - inside padding
             ipady=15,  #ipadx/ipady - inside padding
             padx=10, #padx/pady - outside spacing
             pady=20) #padx/pady - outside spacing

# Functions
def insert_value(value): # Runs when a button is clicked (if we press a number it appears on the screen)
    display.insert(END, value) # (value - number or operator clicked) & (END - add value at the end of display)

def clear_display(): # Clears everything on the screen (from starting position "0" to last position "END" everything will be cleared)
    display.delete(0, END) # (0 → starting position) (END → till last character)

def calculate(): # Runs when = is pressed.
    try: # tells python to run the code and if error happens , dont crash
        result = eval(display.get()) # Reads the screen text and calculates it
        clear_display() # Clears old text and shows result
        display.insert(END, result) # Clears old text and shows result
    except: #this whole shows error when error occurs instead of crashing 
        clear_display() ## Clears old text
        display.insert(END, "Error") # shows error

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
