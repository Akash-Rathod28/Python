books = ["Ramayana", "Mahabharath", "Bhagavadhgitha", "Quran", "The ancient Weapon", "The Gaurdian Angel", "The Biopic of Ambedkar"]

u = 1
for i in books:
    
    print(f"{u}. {i}")
    if u < len(books):
        u += 1
user_choice = input("Which book are you interested in reading? ").strip()
if user_choice.lower() in [b.lower() for b in books]:
    print("Price of this book is $2500")
    user_confirm = input("Do you like to buy this book? (y/n): ").lower()
    
  
    if user_confirm == 'y':
        print("Thank you for buying this book!")
    else:
        print("Maybe next time!")
else:
    print("Sorry, that book is not in our collection.")
