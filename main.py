import os

UI = '''
Enter:
"add" for addition
"sub" for subtraction
"mul" for multiplication
"div" for division
any other text for quiting 
'''

def add(operand1, operand2):
    return operand1 + operand2

def sub(operand1, operand2):
    return operand1 + operand2

def mul(operand1, operand2):
    return operand1 + operand2

def div(operand1, operand2):
    return operand1 + operand2

def continue_calculator():
    userOption = input("Do you want to continue? (yes/any other text for quitting): ")
    if userOption == "yes":
        os.system("clear")
        return True
    else:
        return False

while True:
    operend1 = int(input("enter first operand: "))
    operend2 = int(input("enter second operand: "))
    userOption = input(UI)
    if userOption == "add":
        print(add(operand1=operend1, operand2=operend2))
        if not continue_calculator():
            break 
    elif userOption == "sub":
        print(sub(operand1=operend1, operand2=operend2))
        if not continue_calculator():
            break 
    elif userOption == "mul":
        print(mul(operand1=operend1, operand2=operend2))
        if not continue_calculator():
            break 
    elif userOption == "div":
        print(div(operand1=operend1, operand2=operend2))
        if not continue_calculator():
            break 
    else:
        break
