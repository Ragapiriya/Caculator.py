#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
import math
history_list = []
def history(history_list):
    if len(history_list) >0:
        for i in history_list:
            print(i)
    else:
        print("No past calculations to show")

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
            print(first_operand)
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
            print(second_operand)
        second_operand = float(second_operand)
        
        return first_operand,second_operand
    except ValueError:
        print("Not a valid number,please enter again")


def addition(first_operand,second_operand):
    addition_answer=str(first_operand) +" + "+ str(second_operand) +" = "+ str(first_operand+second_operand)
    print(addition_answer)
    history_list.append(addition_answer)
def substraction(first_operand,second_operand):
    substraction_answer=str(first_operand) +" - "+ str(second_operand) +" = "+ str(first_operand-second_operand)
    print(substraction_answer)
    history_list.append(substraction_answer)
def multiplication(first_operand,second_operand):
    multiplication_answer=str(first_operand) +" * "+ str(second_operand) +" = "+ str(first_operand*second_operand)
    print(multiplication_answer)
    history_list.append(multiplication_answer)
def division(first_operand,second_operand):
    if second_operand != 0:
        division_answer1=str(first_operand) +" / "+ str(second_operand) +" = "+ str(first_operand/second_operand)
        print(division_answer1)
        history_list.append(division_answer1)
    else:
        division_answer2 = str(first_operand)+" / "+str(second_operand)+" = None"
        print("float division by zero")
        print(division_answer2)
        history_list.append(division_answer2)
def power(first_operand,second_operand):
    power_answer=str(first_operand) +" ^ "+ str(second_operand) +" = "+ str(math.pow(first_operand,second_operand))
    print(power_answer)
    history_list.append(power_answer)
def remainder(first_operand,second_operand):
    remainder_answer=str(first_operand) +" % "+ str(second_operand) +" = "+ str(math.remainder(first_operand,second_operand))
    print(remainder_answer)
    history_list.append(remainder_answer)
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
                    division(first_operand,second_operand)
                if choice == "^":
                    power(first_operand,second_operand)
                if choice == "%":
                    remainder(first_operand,second_operand)
    elif choice == "#":
       return -1
    elif choice == "$":
        print("Resetting...")
    elif choice =="?":
        history(history_list)
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
  print("9.History  : ? ")
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if select_op(choice) == -1:
    #program ends here
    print("Done. Terminating")
    exit()
  
