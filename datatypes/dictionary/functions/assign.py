# def introduce(name,age, course):
#  print(f'My name is {name},')
#  print(f'I am {age} old.')
#  print(f'I am studying {course}.')
# introduce('Joseph', 20, 'python') 
# print('\n')
# introduce('Sylvia', 20, 'python') 
# print('\n')

# def multiply(a, b):




def multiply_all(*args):
     result = 1
     for num in args:
         result *=num
     return result

print(multiply_all(3, 4, 5, 6))

def student(name, age):
 print(f"Student name: {name}")
 print(f"Student age: {age}")

student("Alice", 25)

def student_info(**kwargs):
 for key, value in kwargs.items():
  print(f"{key}: {value}")

student_info(name="Alice", age=25, course="Computer Science", university= "MIT" )
