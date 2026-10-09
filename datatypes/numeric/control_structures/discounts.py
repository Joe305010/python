def calculate_discount():
  amount = float(input("Enter the amount:"))
  if amount >= 1000:
    member = input("Are you a member? (yes/no):").lower()
    if member == "yes":
      discount = .2
    elif member == "no":
      discount = .1
    else:
      print("For goods under 999 no discount is given.")
      discount = .0
  else:
    discount = .0
  final_amount = amount - (amount * discount)
  print("Final Price:" ,final_amount)      
calculate_discount()  



