#!/usr/bin/env python3

# Colors
blue="\033[34m"
green="\033[32m"
reset="\033[0m"

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    print("No se puede dividir entre 0.\n")
    return None

def modulus(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def handle_operation(option, num1, num2):
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: modulus,
        6: power
    }

    if option in operations:
        return operations[option](num1, num2)
    return 0

def handle_repeat():
    print("1. Repetir")
    print("2. Salir")
    repeat = int(input("¿Quieres hacer otra operación? "))

    if repeat == 1:
        return True
    return False

def main():
    isRepeat = True

    while isRepeat:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Modulo")
        print("6. Exponente")

        option = int(input("Introduce el valor de la operación: "))

        result = handle_operation(option, num1, num2)

        if result != None:
            print("El resultado de la operación es:", result, "\n")

        isRepeat = handle_repeat()

if __name__ == "__main__":
    main()
