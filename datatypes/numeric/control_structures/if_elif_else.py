# syntax of if=elif=else statement in Python is as follows:
condition1 = True
condition2 = False
if condition1:
 pass
elif condition2:
 pass
else:
 pass

number = 0
if number > 0:
  print(f"{number} is a positive number")
elif number < 0:
  print(f"{number} is a negative number")
else:
  print(f"{number} is zero")
#  example in a function
def check_number(number):
  if number > 0:
    print(f"{number} is a positive number")
  elif number < 0:
    print(f"{number} is a negative number")
  else:
    print(f"{number} is zero")
check_number(5)
check_number(-3)
check_number(0)