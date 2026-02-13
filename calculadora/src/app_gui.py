#!/usr/bin/env python3

import tkinter as tk

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    return "Error"

def modulus(num1, num2):
    if num2 != 0:
        return num1 % num2
    return "Error"

def power(num1, num2):
    return num1 ** num2

current_input = ""
first_number = None
operation = None

def format_result(result):
    """Elimina decimales innecesarios"""
    if isinstance(result, float):
        if result.is_integer():
            return str(int(result))
        else:
            return str(result)
    return str(result)

def press_number(num):
    global current_input

    if num == "." and "." in current_input:
        return

    current_input += str(num)
    update_display(current_input)

def press_operation(op):
    global first_number, current_input, operation
    if current_input != "":
        first_number = float(current_input)
        operation = op
        current_input = ""
        update_display(op)

def press_equal():
    global first_number, current_input, operation

    if first_number is not None and current_input != "":
        second_number = float(current_input)

        if operation == "+":
            result = add(first_number, second_number)
        elif operation == "-":
            result = subtract(first_number, second_number)
        elif operation == "x":
            result = multiply(first_number, second_number)
        elif operation == "/":
            result = divide(first_number, second_number)
        elif operation == "%":
            result = modulus(first_number, second_number)
        elif operation == "^":
            result = power(first_number, second_number)
        else:
            result = "Error"

        result = format_result(result)

        update_display(result)
        current_input = result
        first_number = None
        operation = None

def clear():
    global current_input, first_number, operation
    current_input = ""
    first_number = None
    operation = None
    update_display("")

def backspace():
    global current_input
    current_input = current_input[:-1]
    update_display(current_input)

def update_display(value):
    display.delete(0, tk.END)
    display.insert(0, str(value) + " ")

root = tk.Tk()
root.title("Calculadora")
root.geometry("322x425")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

bg_numbers = "#2d2d2d"
bg_operators = "#3a3a3a"
bg_equal = "#0078D7"
bg_clear = "#d13438"
bg_back = "#444444"
fg_text = "white"

display = tk.Entry(
    root,
    font=("Arial", 20),
    bd=0,
    relief=tk.FLAT,
    justify="right",
    bg="#000000",
    fg="white",
    insertbackground="white",
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('^', 1, 3),

    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('x', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in buttons:

    if text.isdigit() or text == ".":
        bg_color = bg_numbers
        action = lambda x=text: press_number(x)

    elif text == "=":
        bg_color = bg_equal
        action = press_equal

    elif text == "C":
        bg_color = bg_clear
        action = clear

    elif text == "⌫":
        bg_color = bg_back
        action = backspace

    else:
        bg_color = bg_operators
        action = lambda x=text: press_operation(x)

    tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        bg=bg_color,
        fg=fg_text,
        activebackground="#505050",
        activeforeground="white",
        bd=0,
        relief=tk.FLAT,
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
