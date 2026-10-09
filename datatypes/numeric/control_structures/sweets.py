def select(john,jane,james):
 if john > jane: 
  both = john + jane 
  print(f"John and Jane have {both} sweets in total.")

  if john > james:
    print(f"John has more sweets than James and Jane.")
  else:
    print(f"John has less sweets than James")
 elif jane > james:
  print(f"Jane has more sweeets than James")
 elif john == jane and john == james:
  print(f"John, Jane and James have the same amount of sweets.")
 else:
  print(f"James has most sweets than John and Jane.") 


select(25, 15, 20)
select(10, 5, 20)
select(10, 50, 20)
select(50, 50, 20)   