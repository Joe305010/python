def calculate_VAT():
 amount = float(input("Enter amount please:"))
 category = input("Please input your region of origin(Local,African,Overseas):").lower()
 if category == "local":
    VAT = .16
 elif category == "africa":
   VAT = .20
 elif category == "overseas":  
   VAT = .25
 else:
   print("Please make sure that you are from within the valid regions i.e local, africa, overseas")
   return
 VAT_amount = amount * VAT
 final_amount = amount + VAT_amount

 print(f"Original amount: {amount}")
 print(f"VAT: {VAT_amount}")
 print(f"Final amount: {final_amount}")
calculate_VAT()       