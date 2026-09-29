empty_dict = {}
# print(empty_dict)
# print(type(empty_dict))

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(my_dict)
# print(type(my_dict))

big_dict = {
    'name': 'Alice', 
    'age': 25,
    'city': 'Nairobi',
    'country': 'Kenya',
    'hobbies': ['reading', 'traveling', 'cooking'],
}
print(big_dict)

nested_dict = {
    'user': {
        'name': 'Alice',
        'age': 25
    },
    'location': {
        'city': 'Nairobi',
        'country': 'Kenya',
        'coordinates': {
            'latitude': -1.2921,
            'longitude': 36.8219
        }
    }
}
print(nested_dict)
# Accessing values in a dictionary
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30

# Accessing nested dictionary values
print(nested_dict['user']['name'])  # Output: Alice
print(nested_dict['location']['city'])  # Output: Nairobi