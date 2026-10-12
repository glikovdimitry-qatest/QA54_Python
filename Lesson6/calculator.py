#only performs calculator
from Lesson6.exceptions import result


def calculator(a:float,b:float,operator:str):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b #ZeroDivisionError
    raise ValueError("Invalid operator")

#parsing convert string into numbers
def pars(a_str:str,b_str:str,operator:str):
    a = float(a_str) #Value error
    b = float(b_str) #Value error
    return calculator(a,b,operator)

#dialog
def run():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        operator = input("Enter Action operator: (+,-,*,/) ")
        result = pars(a,b,operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError:
        print(f"Cannot divide by 0")
run()