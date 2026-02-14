Name = "Akash Rathod" # string
Age = 20 #int
is_student = True #boolean
weight = 59.6 #float
x = None # none type
print(type(Name)) #it prints <class str>
print(type(Age)) #it print <class int>
print(type(is_student)) #it prints <class boolean>
print(type(weight)) #it prints <class float>
print(type(x)) #it prints <class NoneType>

A = int(input("Enter a value of A: ")) #takes input of A
B = int(input("Enter a value of B: ")) #takes input of B
print(f"The Addition of {A} + {B} = {A+B}") # returns A + B = 13
print(f"The Subraction of {A} - {B} = {A-B}") # returns A - B = 7
print(f"The Multiplication of {A} * {B} = {A*B}") # returns A * B = 30
print(f"The Division of {A} / {B} = {A/B}") # returns A / B = 3.33333333.....
print(f"The Floar Division of {A} // {B} = {A//B}") # returns A // B = 3 (Floor Division)
print(f"The Modules of {A} % {B} = {A%B}") # returns A % B = 1 (Modulus Remiander)
print(f"The Exponential of {A} ** {B} = {A**B}") # returns A ** B = 1000

print(A+B-A+B*2**3) #returns 27
