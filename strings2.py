#1 
user = input("Enter a name")
a = user.replace(" ","")
# count = 0
# for ch in user:
    
#     count += 1
print(len(a))


#2
count = 0
user = input("Enter a sentences").lower()

# for ch in user:
#     if ch == "a":
#         count += 1
print(user.count("a"))

print(count)

#3
str = input("Enter a string:")
a = str.replace(" ","-")
print(a)

#4
user = input("Enter a input")
if user.endswith("ing"):
    print("Yes")
else:
    print("No")

#5
user = input("Enter the sentences")
# word = 0
# for i in user.split(" "):
    
#         word+=1
# print(word)
print(len(user.split()))


#6
# user = input("Enter a string:")

for ch in user:
    if ch.isdigit():
        print(ch, end="")

#7
passuser = input("enter a sentences")
vowels = "aeiouAEIOU"
result = ""
for ch in user:
    if ch not in vowels:
        result += ch
print(result)

#8
valid = True
for ch in user:
    if not (ch.isalpha() or ch.isspace()):
        valid = False

if valid:
    print("Valid")
else:
    print("Invalid")

#9
str = input("Enter a string:")
print(str.istitle())
print(str.swapcase())
print(str.title())


#10
user = input()
words = user.split()
result = []

for w in words:
    result.append(w[::-1])

print(" ".join(result))

