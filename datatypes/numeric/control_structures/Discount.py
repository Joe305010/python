def calculate_discount():
    amount = float(input("Enter the amount: "))
    membership = input("Are you a member? (yes/no): ").lower()

    if amount > 1000:
        if membership == "yes":
            discount = amount * 0.20
        elif membership == "no":
            discount = amount * 0.10
        else:
            discount = 0
    else:
        discount = 0

    final_amount = amount - discount

    print(f"Original amount: {amount}")
    print(f"Discount: {discount}")
    print(f"Final amount: {final_amount}")


calculate_discount()