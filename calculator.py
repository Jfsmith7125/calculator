import tkinter as tk
from math import sqrt

# Global variables for the current calculation and memory value
calculation = ""
memory = 0

def add_to_calculation(symbol):
    """Add a symbol to the current calculation and update the display."""
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    """Evaluate the current calculation and update the display."""
    global calculation
    try:
        calculation = str(eval(calculation.replace('^', '**')))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))

def clear_field():
    """Clear the current calculation and the display."""
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def square_root():
    """Calculate the square root of the current calculation and update the display."""
    global calculation
    try:
        calculation = str(sqrt(float(eval(calculation))))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))

def square():
    """Square the current calculation and update the display."""
    global calculation
    try:
        calculation = str(float(eval(calculation))**2)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))

def reciprocal():
    """Calculate the reciprocal of the current calculation and update the display."""
    global calculation
    try:
        calculation = str(1/float(eval(calculation)))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        calculation = ""
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))

def memory_clear():
    """Clear the memory."""
    global memory
    memory = 0

def memory_recall():
    """Display the current memory value."""
    global memory
    text_result.delete(1.0, "end")
    text_result.insert(1.0, str(memory))

def memory_add():
    """Add the current calculation to the memory."""
    global memory, calculation
    memory += float(eval(calculation))

def memory_subtract():
    """Subtract the current calculation from the memory."""
    global memory, calculation
    memory -= float(eval(calculation))

# Create the main window
root = tk.Tk()
root.geometry("330x335")
root.title("My Calculator")

# Create the text field for the display
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=6)

# Define the buttons
buttons = [
    ('MC', 'MR', 'M+', 'M-', 'MS'),
    ('%', 'CE', 'C', '⌫', '1/x'),
    ('x^2', '√x', '7', '8', '9'),
    ('/', '4', '5', '6', '*'),
    ('-', '1', '2', '3', '+'),
    ('±', '0', '.', '=', 'sqrt'),
]

# Create the buttons and add them to the window
for i, button_row in enumerate(buttons):
    for j, button_text in enumerate(button_row):
        if button_text == 'sqrt':
            button = tk.Button(root, text=button_text, command=square_root, width=5, font=("Arial", 14))
        elif button_text == 'x^2':
            button = tk.Button(root, text=button_text, command=square, width=5, font=("Arial", 14))
        elif button_text == '1/x':
            button = tk.Button(root, text=button_text, command=reciprocal, width=5, font=("Arial", 14))
        elif button_text == 'MC':
            button = tk.Button(root, text=button_text, command=memory_clear, width=5, font=("Arial", 14))
        elif button_text == 'MR':
            button = tk.Button(root, text=button_text, command=memory_recall, width=5, font=("Arial", 14))
        elif button_text == 'M+':
            button = tk.Button(root, text=button_text, command=memory_add, width=5, font=("Arial", 14))
        elif button_text == 'M-':
            button = tk.Button(root, text=button_text, command=memory_subtract, width=5, font=("Arial", 14))
        elif button_text == 'C':
            button = tk.Button(root, text=button_text, command=clear_field, width=5, font=("Arial", 14))
        else:
            button = tk.Button(root, text=button_text, command=lambda text=button_text: add_to_calculation(text), width=5, font=("Arial", 14))
        button.grid(row=i+2, column=j+1, padx=(5 if j == 0 else 0, 0))

# Start the main event loop
root.mainloop()
