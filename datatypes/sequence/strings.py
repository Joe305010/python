s = "Welcome to the world of programming!"
print(s)
print(type(s))

s2 = 'This is a string in Python'
print(s2)
print(type(s2))

s3 = '''This is a multi-line string in Python.'''
print(s3)
print(type(s3)) 

s4 = """This is also a multi-line string in Python."""
print(s4)
print(type(s4))

# string breakers
s5 = "This is a string\
  that is broken into\
      multiple lines."
print(s5)
print(type(s5))

s6 = 'This is a broken string\
  that is broken into\
      multiple lines.'
print(s6)
print(type(s6))

single_quote_string = 'This is a string with \nsingle quotes.'
print(single_quote_string)

double_quote_string = "This is a string with \ndouble quotes."
print(double_quote_string)

escaped_string = 'This is a string with an \'escaped\' newline character.'
print(escaped_string)

double_escaped_string = "This is a string with an 'escaped' newline character."
print(double_escaped_string)

tabbed_string = "This is a string with a \ttab character."
print(tabbed_string)

# string concatenation
s7 = "Hello, " + "world!"
print(s7)

first_name = "Joseph"
last_name = "Mwangi"
full_name = first_name + " " + last_name
print(full_name)

student_name = "Joseph Mwangi"
fees_balance = 10000
sms = " Hello " + student_name + ", your fees balance is " + str(fees_balance) + "."
print(sms)

#string formatting using the f-string
sms_f = f" Hello {student_name}, your fees balance is {fees_balance}."
print(sms_f)

name = "Joseph"
age = 20
info = f"My name is {name} and I am {age + 1} years old."
print(info)


# indexing
sentence = "Welcome to the world of programming!"
print(sentence[0])  # Output: W
print(sentence[7])  # Output: t
print(sentence[-1])  # Output: !
print(sentence[-8])  # Output: g
