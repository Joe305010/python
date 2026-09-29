def function_name():
  pass
# These are the parametres for the send_sms function: name and balance
def send_sms(name, balance):
  return f"Hello {name}, your fees balance is ksh.{balance}, please pay by the end of the month"

print(send_sms("Joseph",200 )) #pass the arguments
print(send_sms("Lookie",7500 )) #pass the arguments
print(send_sms("Chris",4200 )) #pass the arguments
print(send_sms("Ian",2000 )) #pass the arguments

  # Default parameters
def send_sms_default(name, balance,due_date="the end of the month"):
    return f"Hello {name}, your fees balance is ksh {balance}, please pay by the {due_date}"

print(send_sms_default("Joseph", 100, "the end of the week"))
print(send_sms_default("Jane", 100)) 