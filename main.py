def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

from art import logo

def calculator():
  calculator_is_running = True
  print(logo)
  operations = {
    "+": add, 
    "-":subtract, 
    "*": multiply, 
    "/": divide
    }

  n1 = float(input("What is the first number?"))

  for key in operations:
    print (key)

  while calculator_is_running == True:

    operation_symbol = input("Please pick an input form the choices above. ")

    n2 = float(input("What is the second number?"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    keep_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ")
    if keep_calculating == "n":
      calculator_is_running = False
      calculator()
    if keep_calculating == "y":
      n1 == answer

calculator()