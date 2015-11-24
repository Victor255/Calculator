"""CALCULATOR"""
import os
import sys

def clear():
    """THIS CLEANS THE SCREEN"""
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("nt",):
        os.system("cls")
clear()

def menu_two():
    menu()
    select_menu()

def menu():
    """SHOWS THE INSTRUCTIONS"""
    print "_____________________________________________"
    print "|Calculator!                                 |"
    print "|Enter 1 if you want to do a sum.            |"
    print "|Enter 2 if you want to do a subtractionion. |"
    print "|Enter 3 if you want to do a multiplication. |"
    print "|Enter 4 if you want to do a division.       |"
    print "|Enter 5 if you want exit of the Calculator. |"
    print "|____________________________________________|"

def optis():
    """SHOWS THE RESPONSE ON THE SCREEN shows"""
    option_one = Enter_number()
    option_two = Enter_number()
    clear()
    print "\nThe answer is:"
    return option_one, option_two

def Enter_number():
    while True:
        answer = raw_input("\nEnter a Number please: ")
        try:
            answer = int(answer)
            return answer
            break
        except ValueError:
            print "\nTry again."

def Incognit():
    """ASK IF THE USER WANTS TO MAKE OTHER OPERATION """
    selected = True
    while selected == True:
        selection = raw_input("\nDo you want to continue to use the calculator? yes or no: ")
        if selection == "y" or selection == "yes":
            clear()
            menu_two()
        elif selection == "n" or selection == "no":
            clear()
            sys.exit(1)
        else:
            print "Insert only yes or no."

#Test1
def sum(numbers):
    """THIS FUNCTION WILL RETURN THE SUM"""
    return numbers[0] + numbers[1]

#Test2
def subtraction(numbers):
    """THIS FUNCTION WILL RETURN THE SUBTRACTION"""
    return numbers[0] - numbers[1]

#Test3
def multiplication(numbers):
    """THIS FUNCTION WILL RETURN THE MULTIPLICATION"""
    return numbers[0] * numbers[1]

#Test4
def division(numbers):
    """THIS FUNCTION WILL RETURN THE DIVISION"""
    return numbers[0] / numbers[1]

def select_menu():
    """MENU OF OPTIONS"""
    opti = Enter_number()
    validate = True
    while validate == True:
        if opti == 1:
            clear()
            print "You are Doing a sum"
            print str(sum(optis()))
            Incognit()
        elif opti == 2:
            clear()
            print "You are Doing a Subtraction"
            print str(subtraction(optis()))
            Incognit()
        elif opti == 3:
            clear()
            print "You are Doing a Multiplication"
            print str(multiplication(optis()))
            Incognit()
        elif opti == 4:
            clear()
            print "You are Doing a Division"
            print str(division(optis()))
            Incognit()
        elif opti == 5:
            clear()
            sys.exit(1)
        else:
            menu_two()

if __name__ == '__main__':
    menu_two()
