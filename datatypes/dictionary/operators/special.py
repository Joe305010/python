# Special Operators - They are divide in to two: Identity and membeeeship operators
# Identity operators:
    # IS-Returns true if both operands are identical
    #  IS NOT- Returns true if the operands are not identical
# Membership Operators:
    # IN - Returns True if a value/variable is found in the sequence.
    # IN NOT - Returns True if a value/variable is not found in the sequence.   
a = 10
b = 20    

# Identity Operators
print(a is b)
print(a is not b)

# Membership Operators
my_list = [1, 2, 3, 10]
print(a in my_list)
print(a not in my_list)


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3=[1, 2, 3]
y3=[1, 2, 3]


print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

message = "Hello, Welcome to Python Programming"
print('Helllo' in message)
print('Python' in message)

dict_example = {'name':'Alice', 'Age': 25}
print('name' in dict_example)
print('address' not in dict_example)
print('Alice' in dict_example)