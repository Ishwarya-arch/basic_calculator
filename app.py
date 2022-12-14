#--- imports
from datetime import datetime

List_equations=[]

#functions for operations
def validate_input(given_num1, given_num2):
    if given_num1.isnumeric() and given_num2.isnumeric():
        return True, float(given_num1), float(given_num2)
    else: 
        print("Please enter valid Number")
        return False, 0, 0

def add(a,b):
    res, a, b = validate_input(a,b)
    
    if res:
        return(a+b)
    else: 
        print("\nPlease enter valid input (integer/ float): ")
        return 0

def sub(a,b):
    res, a, b = validate_input(a,b)
    
    if res:
        return(a-b)
    
    else: 
        print ("\nPlease enter Valid float/ integer :  ")
        return 0
    
def mul (a,b):
    res, a, b = validate_input(a,b)
    
    if res:
        return(a*b)
    
    else: 
        print ("\nPlease enter Valid float/ integer :  ")
        return 0

def div(a,b):
    res, a, b = validate_input(a,b)
    
    if res and b!=0:
        return(a/b)
    
    else: 
        print ("\nPlease enter Valid float/ integer :  ")
        return 0

def operator_is_valid(input_op):
    if input_op in operators.keys():
        return True
    else:
        return False

def calculate():
    
    print("\n\n")
    
    #getting input from user
    num1=input(" Enter first number: ")
    given_operator= input("Select an Operator [ +, -, *, / ]: ")
    num2= input(" Enter second number: ")
    
    #calling the operator functions:
    if operator_is_valid(given_operator):
        result= operators[given_operator](num1, num2)
        #output with format:
        equation = "\nEquation: {} {} {} = {}".format(num1, given_operator, num2, result)
        print(equation)
        List_equations.append(equation)


    else:
        print("Operator is invalid")


operators = {"+":add,
             "-":sub,
            "*":mul,
            "/":div}

#getting user input
if __name__== "__main__":
    calculate()
    while True:
        answer= input("Do you want to continue [ Y/N ]: ")

        if answer== "Y" or answer=="y":
            print("\nDoing calculation again")
            calculate()
        
        elif answer== "N" or answer=="n":
            for i in range(len(List_equations)):
                print(List_equations[i])
                print()
            
            print("\ntoodaloo!")
            file_name = datetime.now().strftime("Ca-%Y_%m_%d-%I_%M_%S_%f.txt")

            current_file= open(file_name,"w")
            for i in range(len(List_equations)):
                current_file.write(List_equations[i])
            current_file.close()
            break
        else:
            print("Invalid input. Try again.")
            continue
        
        print("\n\n")
