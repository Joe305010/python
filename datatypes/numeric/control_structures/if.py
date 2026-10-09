# syntax of if
condition = True


if condition:
  pass
car = "Toyota"
if car == "Toyota":
  print("This is a Toyota car")

  # Example in a function:
  def check_car(car):
    if car == "Toyota":
      print("This is a Toyota car")
    check_car("Toyota")
    check_car("Honda")