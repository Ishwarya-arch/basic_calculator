
'''def calc():

    print("5 + 5 = 10\n\n")

while True:

    answer = input("Do you want to continue [Y/N] ")

    if answer == 'Y' or answer == 'y':
        print("I am going to continue")
        calc()
    
    elif answer == 'N' or answer == 'n':
        print ("I am going to exit.")
        break
    else:
        print("Invalid input. Try again.")
        continue'''


def validate_input(given_num1, given_num2):
    while True:
        if given_num1.isnumeric():
            return True, float(given_num1)
            break
        else:
            print("The given input is of type ",type(given_num1))
            print("\nPlease enter a valid Float/Integer: ")
        