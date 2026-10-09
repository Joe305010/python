# Example of nested if elif else statements in Python
number = 10
if number > 0:
  if number % 2 == 0:
    print(f"{number} is a positive and even number")
  elif number % 2 != 0:
    print(f"{number} is a positive and odd number")
  else:
    print(f"{number} is a positive number and neither even nor odd")
elif number < 0:
  if number % 2 == 0:
    print(f"{number} is a negative and even number")
  else:
    print(f"{number} is a negative and odd number")
else:
  print(f"{number} is not a positive number")
