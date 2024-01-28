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
        # Replace '^' with '**' for exponentiation before evaluating
        calculation = str(eval(calculation.replace('^', '**')))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))
    finally:
        # Clear the calculation after evaluation
        calculation = ""

def clear_field():
    """Clear the current calculation and the display."""
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def square_root():
    """Calculate the square root of the current calculation and update the display."""
    global calculation
    try:
        # Check if the calculation is not empty and is a number
        if calculation.strip() and calculation.replace('.', '', 1).isdigit():
            calculation = str(sqrt(float(eval(calculation))))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
            calculation = ""
        else:
            raise ValueError("Invalid input for square root.")
    except Exception as e:
        clear_field()
        text_result.insert(1.0, str(e))

def backspace():
    """Remove the last character from the current calculation and update the display."""
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


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

def memory_store():
    """Store the current calculation in memory."""
    global memory, calculation
    memory = float(eval(calculation))

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
    ('CE', 'C', '%', '/', '⌫'),
    ('7', '8', '9', '-', '^'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '*'),
    ('0', '.', '=', 'sqrt'),
]

for i, button_row in enumerate(buttons):
    for j, button_text in enumerate(button_row):
        if button_text == '=':
            button = tk.Button(root, text=button_text, command=evaluate_calculation, width=5, font=("Arial", 14))
        elif button_text == 'sqrt':
            button = tk.Button(root, text=button_text, command=square_root, width=5, font=("Arial", 14))
        elif button_text == 'MC':
            button = tk.Button(root, text=button_text, command=memory_clear, width=5, font=("Arial", 14))
        elif button_text == 'MR':
            button = tk.Button(root, text=button_text, command=memory_recall, width=5, font=("Arial", 14))
        elif button_text == 'M+':
            button = tk.Button(root, text=button_text, command=memory_add, width=5, font=("Arial", 14))
        elif button_text == 'M-':
            button = tk.Button(root, text=button_text, command=memory_subtract, width=5, font=("Arial", 14))
        elif button_text == 'MS':
            button = tk.Button(root, text=button_text, command=memory_store, width=5, font=("Arial", 14))
        elif button_text == 'CE' or button_text == 'C':
            button = tk.Button(root, text=button_text, command=clear_field, width=5, font=("Arial", 14))
        elif button_text == '⌫':
            button = tk.Button(root, text=button_text, command=backspace, width=5, font=("Arial", 14))
        else:
            button = tk.Button(root, text=button_text, command=lambda symbol=button_text: add_to_calculation(symbol), width=5, font=("Arial", 14))
        button.grid(row=i+2, column=j)


root.mainloop()
