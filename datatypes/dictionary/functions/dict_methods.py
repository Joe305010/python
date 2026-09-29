# 1. get ()
# This method returns the value for the specified key if the key is in the dictionary
# It returns none if the value is not specified

example_dict = {
  'name': 'alice',
  'age': 30,
  'city':'Newyork'
  'hobbies'['reading','travelling','cooking']
}
# print(example_dict.get('name','name not found'))

# 2. keys() - returns a view object with the dictionary keys, allowing efficient access of the keys
print(example_dict.keys())

# 3. values() returns a view object containing value which can be accessed
# print(example_dict.values())

# 4. pop() - removes and retrieves the value linked with a given key from a dictionary
# If the key is not present in the dictionary, you can set an optional default
popped = example_dict.pop("age", None)
# print (popped)
# print(example_dict)

# 5. popitem() - is used to remove and return the last inserted key-value pair
# If the dictionary is empty, it reurns a KeyError
popped_item = example_dict.popitem()

# 6. update() - updates the key-value pairs of the dictionary using elements from another
#  dictionary or an irterable of key-value pairs
example_dict.update({"countrty": "USA"})
print(example_dict)