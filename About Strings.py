a = "Udemy Physics Walaha" # Storing a value in the variable name called a

print(a.upper()) # printing the value all the letters should be in capital if it is lower converted all char to upper

print("---------------")

print(a.lower()) # converting upper ---> lower

print("---------------")

print(a.capitalize()) # converting first letter to capital

print("---------------")

print(a.swapcase()) # converting lower --> upper upper ---> lower

print("---------------")

print(a.title()) # converting each word starting letter capital rest small
print("---------------")

s = "akash"

print(s.isalpha()) # prints True if the string is only alphabets
print("---------------")
s = "893674" 
print(s.isdigit()) # prints True if the string as numbers

print("---------------")
s = "Akash893"
print(s.isalnum()) # prints the string contain both alpha and numeric

print("---------------")
s = "_akash"

print(s.isidentifier()) # checks the entered string is valid indentifier(variable name) or not

print("---------------")

s = "  "

print(s.isspace()) # checks the string contain only spaces

print("---------------")
s = "Akash Rathod"

print(s[::-1]) # it reverse the string

print("---------------")

print(s[1:5]) # it prints the substring of string from 0 to 5-1

print("---------------")

print(s[0]) # it prints the first index of the string

print("---------------")

print(s[-1]) # it prints the last index of the string 

print("---------------")

s = "Akash Rathod"

print(s.startswith("A")) # returns True if it starts with "A" else False

print("---------------")

print(s.endswith("d")) # returns true if ends with "d" else False

print("---------------")

print(s.find("a")) # finds " a " in which index it present if its nots in the string it return -1

print("---------------")

print(s.rfind("u")) # finds " u " in which index is presents it not present in the string it returns -1

print("---------------")

print(s.index("a")) # it is similar like find but if it is not found gives error index not found to avoid this we use find function

print("---------------")

print(s.rindex("a")) # it finds words from right side

print("---------------")

print(s.count("a")) # it counts How many times the word is repeating

print("---------------")

s = "           Akash RAthod               "

print(s)

print(s.strip())

print("---------------")

print(s.lstrip())

print("---------------")

print(s.rstrip())









