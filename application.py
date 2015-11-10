import os
import sys

def menu_two():
    menu()
    select_menu()

def menu():
    os.system("clear")
    print "_____________________________________________"
    print "|Calculator!                                 |"
    print "|Enter 1 if you want to do a sum.            |"
    print "|Enter 2 if you want to do a subtractionion. |"
    print "|Enter 3 if you want to do a multiplication. |"
    print "|Enter 4 if you want to do a division.       |"
    print "|Enter 5 if you want exit of the Calculator. |"
    print "|____________________________________________|"

def optis():
    option_one = Enter_number()
    option_two = Enter_number()
    print "\nThe answer is:"
    return option_one, option_two

def Enter_number():
    while True:
        answer = raw_input("\nEnter a option please: ")
        try:
            answer = int(answer)
            return answer
            break
        except ValueError:
            print "\nTry again."
def Incognit():
    selected = True
    while selected == True:
        selection = raw_input("Do you want make other operation? yes or no: ")
        if selection == "y" or selection == "yes":
            menu_two()
        elif selection == "n" or selection == "no":
            sys.exit(1)
        else:
            print "Insert yes or no."

def select_menu():
    opti = Enter_number()
    validate = True
    while validate == True:
        if opti == 1:
            print str(sum(optis()))
            Incognit()
        elif opti == 2:
            print str(subtraction(optis()))
            Incognit()
        elif opti == 3:
            print str(multiplication(optis()))
            Incognit()
        elif opti == 4:
            print str(division(optis()))
            Incognit()
        elif opti == 5:
            print "Good bye"
            sys.exit(1)
        else:
            menu_two()

def sum(numbers):
    return numbers[0] + numbers[1]

def subtraction(numbers):
    return numbers[0] - numbers[1]

def multiplication(numbers):
    return numbers[0] * numbers[1]

def division(numbers):
    return numbers[0] / numbers[1]

if __name__ == '__main__':
    menu_two()
