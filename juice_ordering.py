import random

order_list = []
count = 1
cost_one_juice = 20

first_juice = input("Enter the juice you want to order (Cost: $20): ")
order_list.append(first_juice)

while True:
    choice = input("Do you want to add another juice? (y/n): ").lower()

    if choice == 'y':
        juice = input("Enter the juice you want to order: ")
        order_list.append(juice)

    elif choice == 'n':
        print("Thank you for visiting... Have a nice day 😊")
        break

    else:
        print("Please enter only y or n.")

print("\nYou ordered:")
for item in order_list:
    print(f"{count}. {item}")
    count += 1

total_cost = cost_one_juice * len(order_list)
gift = random.choice(order_list)

print(f"\nCost of your order is: ${total_cost}")
print(f"This is your free gift for visiting: {gift} 🎁")
