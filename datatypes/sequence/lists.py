empty_list = []
print(empty_list)
print(type(empty_list))

# list with elements
numbers = [1, 2, 3, 4, 5]
print(numbers)

#list with strings
fruits = ['apple', 'banana', 'cherry']
print(fruits)

#list with mixed data types
mixed_list = [1, 'apple', 3.14, True]
print(mixed_list)

# nested list
nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print(nested_list)

#accessing elements of a list
print(numbers[0])  # first element
print(fruits[-1])  # last element
print(mixed_list[1])  # second element
print(nested_list[2])  # third sublist

 # list slicing
print(numbers[1:4])  # elements from index 1 to 3
print(fruits[0:2])  # elements from index 0 to 1
print(mixed_list[:2])  # first three elements
print(nested_list[1][1:3])  # elements from index 1 to 2