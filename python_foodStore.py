import random

food = ["Dosa", "Porata sagu", "Pulav", "Eggrice", "Biryani", "Chiken Kabbab", "Kushka"]
num = 1

# Display the menu
for i in food:
    print(f"{num}. {i}")
    num += 1 

user = input("\nDo you want to pick a food at random? (y/n): ").lower()

if user == 'y':
    # Correct way to pick a random item from a list
    a = random.choice(food) 
    
    print(f"The random selection is: {a}")
    user1 = input(f"Do you want to order {a}? (y/n): ").lower()
    
    if user1 == 'y':
        print("Payable amount is $200.")
        print("Thank you for your order!")
    else:
        print("No problem. Maybe something else next time.")
else:
    print("No worries, take your time looking at the menu.")

print("Have a good day!")
