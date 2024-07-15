#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
import math
def operandsInput():
    try:
        first_operand = input("Enter first number: ")
        if '$' in first_operand:
            print(first_operand)
            return None, None
        elif '#' in first_operand:
            print(first_operand)
            print("Done. Terminating")
            raise SystemExit
        else:
            print(int(first_operand))
        first_operand= float(first_operand)
        
        second_operand = input("Enter second number: ")
        if '$' in second_operand:
            print(second_operand)
            return None, None
        elif '#' in second_operand:
            print(second_operand)
            print("Done. Terminating")
            raise SystemExit
        else:
            print(int(second_operand))
        second_operand = float(second_operand)
        
        return first_operand,second_operand
    except ValueError:
        print("Not a valid number,please enter again")


def addition(first_operand,second_operand):
    print(str(first_operand) +" + "+ str(second_operand) +" = "+ str(first_operand+second_operand))
def substraction(first_operand,second_operand):
    print(str(first_operand) +" - "+ str(second_operand) +" = "+ str(first_operand-second_operand))
def multiplication(first_operand,second_operand):
    print(str(first_operand) +" * "+ str(second_operand) +" = "+ str(first_operand*second_operand))
def divion(first_operand,second_operand):
    if second_operand != 0:
        print(str(first_operand) +" / "+ str(second_operand) +" = "+ str(first_operand/second_operand))
    else:
        print("float division by zero")
        print(str(first_operand)+" / "+str(second_operand)+" = None")
def power(first_operand,second_operand):
    print(str(first_operand) +" ^ "+ str(second_operand) +" = "+ str(math.pow(first_operand,second_operand)))
def remainder(first_operand,second_operand):
    print(str(first_operand) +" % "+ str(second_operand) +" = "+ str(math.remainder(first_operand,second_operand)))
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice in ["+","-","*","/","^","%"]:
        operands=operandsInput()
        if operands:
            first_operand, second_operand = operands
            if first_operand is not None and second_operand is not None:
                if choice == "+":
                    addition(first_operand,second_operand)
                if choice == "-":
                    substraction(first_operand,second_operand)
                if choice == "*":
                    multiplication(first_operand,second_operand)
                if choice == "/":
                    divion(first_operand,second_operand)
                if choice == "^":
                    power(first_operand,second_operand)
                if choice == "%":
                    remainder(first_operand,second_operand)
    elif choice == "#":
       return -1
    elif choice == "$":
        print("Resetting...")
    else:
        print("Unrecognized operation")



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if select_op(choice) == -1:
    #program ends here
    print("Done. Terminating")
    exit()
  
