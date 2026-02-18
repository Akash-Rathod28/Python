#1
string3 = "Chat Gpt"
print(len(string3))
print(string3[0])
print(string3[-1])

#2
user = input("Enter Your Name:")
print(user.lower())
print(user.upper())

#3
str3 = input("Enter a string")
if str3 == "":
    print("Empty String")
else:
    print("Not empty")

#4
user = input("Enter a name:")
if user == "python":
    print("Correct")
else:
    print("Wrong")

#5
user = input("Enter a string:")
if len(user) > 10:
    print("Long String")
else:
    print("Short String")
#6
user = input("enter a string:")
if "a" in user:
    print("Contains a")
else:
    print("Doesn't contain a")

#7
user = input("Enter a string:")
if len(user) > 0 and user[0] == user[-1]:
    print("Same")
else:
    print("Different")

#8
user = input("Enter a string:")
if user.isdigit():
    print("digits")
elif user.alpha():
    print("Alphabet")
else:
    print("Missed")

#9
user = input("Enter a string ")
a = user.copy()
c = a.reverse()
if a == c:
    print("it is palindrome")
else:
    print("It is not palindrome")

#10
user1 = input("Enter a string")
if user1[0] == 'A' or user1[0] == 'a':
    print("Starts with a")
else:
    print("Does not starts with a")


#11
user = input("Enter atleast 8 characters including numbers")
has_digit = False
for ch in user:
    if ch.isdigit():
        has_digit = True

if len(user) >= 8 and has_digit:
    print("Strong password")
else:
    print("Weak password")


#12
vowels = ["a","e","i","o","u"]
user = input("Enter a sentences")


vowel_count = 0
consonant_count = 0

for ch in user.lower():
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1

#13
user = input("Enter a string").strip()
s = user.replace(" ", "") # to remove the spaces without strip
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



#14 to check valid indentifier(variales/not)
user = input("Enter a valid identifier or not")
if user.isidentifier():
    print("Valid")
else:
    print("Invalid")


#15
user = input("Enter a string")
if user.islower():
    print("Lowercase only")
elif user.isupper():
    print("Uppercase only")
else:
    print("Mixed case")



user = "cac"
print(user[::-1])
