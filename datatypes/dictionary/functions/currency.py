currencies = ["USD", "EUR", "TSH", "UGX", "KES"]

def convert_to_ksh(amount, from_currency, rates_to_ksh):
  print('This is the conversion result:\n')
  return amount * rates_to_ksh
print(convert_to_ksh(1000, 'USD', 140))