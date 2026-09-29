empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

numbers = (1, 2, 3, 4, 5)
print(numbers)

fruits = ('apple', 'banana', 'cherry')
print(fruits)

mixed_tuple = (1, 'apple', 3.14, True)
print(mixed_tuple)

nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (True, False))
print(nested_tuple)

# accessing elements of a tuple
print(numbers[0])  # first element
print(fruits[1])   # second element
print(mixed_tuple[2])  # third element
print(nested_tuple[2][1])  # second subtuple
print(nested_tuple[0][2])  # third element of first subtuple
print(nested_tuple[1][1])  # second element of second subtuple


# immutability of tuples
# trying to change an element of a tuple will raise an error
# numbers[0] = 10  # this will raise a TypeError

# tuple slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # elements from index 1 to 3
print(numbers[:3])   # elements from the beginning to index 2
print(numbers[2:5])  # elements from index 2 to 4
print(numbers[::2])  # every second element
print(numbers[::-1])  # reversed tuple