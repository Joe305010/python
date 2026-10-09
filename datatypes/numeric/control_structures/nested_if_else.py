# Example of nested if statements in Python
number = 10
if number > 0:
  if number % 2 == 0:
    print(f"{number} is a positive and even number")
  else:
    print(f"{number} is a positive and odd number")
else:
  if number % 2 == 0:
    print(f"{number} is a negative and even number")
  else:
    print(f"{number} is a negative and odd number")

def check_number(number):
  if number > 0:
    if number % 2 == 0:
      print(f"{number} is a positive and even number")
    elif number % 2 != 0:
      print(f"{number} is a positive and odd number")
  else:
    if number % 2 == 0:
      print(f"{number} is a negative and even number")
    else:
      print(f"{number} is a negative and odd number")

check_number(10)
check_number(-7)
check_number(0)
check_number(-8)