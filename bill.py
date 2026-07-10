items = []
prices = []
quantities = []

while True:
    item = input("Enter your food or (q to quit): ")
    if item.lower() == "q":
        print("Exited the cart")
        break
    else:
        price = float(input(f"Enter the price of {item}: "))
        quantity = int(input(f"Enter the quantity of {item}: "))
        items.append(item)
        prices.append(price)
        quantities.append(quantity)

print("\nBill")
print("-" * 50)
total = 0

for i in range(len(items)):
    print(f"Item: {items[i]}")
    print(f"Price: ₹{prices[i]}")
    print(f"Quantity: {quantities[i]}")
    print(f"Subtotal: ₹{prices[i] * quantities[i]}")
    print("-" * 50)
    total += prices[i] * quantities[i]

print(f"The total bill is ₹{total}")

        
        



