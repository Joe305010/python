def check_grade():
  marks = int(input("Enter your marks: "))
  if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
  elif marks >= 90:
    print("You have scored an A.")
  elif marks >= 80:
    print("You have scored a B.")
  elif marks >= 70:
    print("You have scored a C.")
  elif marks >= 60:
    print("You have scored a D.")
  else:
    print("You have scored an F.")
