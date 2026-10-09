def grade_checker(marks):
  if 0 <= marks <= 100:
   if marks >= 90:
     print(f"{marks} is an A grade.")
   elif marks >= 80:
     print(f"{marks} is a B grade.")
   elif marks >= 70:
     print(f"{marks} is a C grade.")
   elif marks >= 60:
     print(f"{marks} is a D grade.")
   else:
     print(f"{marks} is an F grade.")
  else:
   print(f"{marks} is an invalid mark.")
grade_checker(95)
grade_checker(85)
grade_checker(75)
grade_checker(65)
grade_checker(55)

