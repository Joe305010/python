def age_checker(age):
  if age >=18:
    print(f"{age} is an adult.")
    if age >= 60:
      print(f"{age} is a senior citizen.")
    elif age >= 35:
      print(f"{age} is a middle-aged adult.")
    else:
      print(f"{age} is a young adult.")
  else:
    print(f"{age} is a minor.")

age_checker(15)
age_checker(25)
age_checker(40)
age_checker(65)    