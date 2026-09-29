# Types of functions in python
# 1. User-defined funtions 
def function_name():
  print("Function is called")

# function_name()
# 2. built-in functions
# example: len()
print(len("Hello"))


# 3. Anonymous Function (lambda function)
# Example: lambda x:x + 1
increment = lambda x: x + 1
print(increment(5))

multiply = lambda x, y:x * y
print(multiply(3,4))

# recursive function
# Example: factorial
def factorial(n):
  if n ==0:
    return 1
  else: return n* factorial(n-1)

  print(factorial(5))