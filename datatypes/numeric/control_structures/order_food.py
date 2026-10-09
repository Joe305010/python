def order_food():
  category = input("Hello and welcome to \n Hilton Dishes.\nChoose category (Food/Stew/Drinks): ")
  # Food section
  if category.lower() == "food":
    food = input("Choose your food (Ugali/Rice/Chapati): ")
    if food.lower() == "ugali":
      print("You have ordered Ugali.")
    elif food.lower() == "rice":
      print("You have ordered Rice.")
    elif food.lower() == "chapati":
      print("You have ordered Chapati.")

    else:
      print("Food not available currently")
      # Stew Section
  elif category.lower() == "stew":
    stew = input("Choose your favourite Stew (Marinated fish, Beans, Green Peas): ")
    if stew.lower() == "marinated fish":
      print("You have ordered Marinated Fish.")
    elif stew.lower() == "beans":
      print("You have ordered Beans.") 
    elif stew.lower == "green peas":
          print("You have ordered Green Peas.")
    else:
      print("Stew not available currently.")


      # Drinks section
  elif category.lower() =="drinks":
    drink = input("Choose your drink(Water/Juice/Soda):")       
    if drink.lower() == "water":
      print('You have ordered Water.')
    elif drink.lower() == "juice":
      print('You have ordered  Juice')
    elif drink.lower() == "soda":
      print('You have ordered Soda')
    else:
      print('Drink not available.')  
  else:
    print("Drink not available currently.")

order_food()    