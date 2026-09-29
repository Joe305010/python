# These are the in-built methods in Python
# 1. Append
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'banana']
fruits.append('orange')
print(fruits)

# 2.Extend
more_fruits = ['mango', 'pineapple']
fruits.extend(more_fruits)
print(fruits)

# 3.Index
index_of_banana = fruits.index('banana')
print(fruits)

# 4. Insert
fruits.insert(2, 'Grapes')
print(fruits)

# 5. Pop
popped_fruit = fruits.pop(0)
print(popped_fruit)
print(fruits)

# 6. Remove
fruits.remove('banana')
print(fruits)

# 7.Reverse
fruits.reverse()
print(fruits)

# 8. Count
count_of_banana = fruits.count('banana')
print(fruits)
  
# 9.Len
length_of_fruits = len(fruits)
print(length_of_fruits)
