a = int(input("Enter a number : "))
b = 1
c = 0
while b<=a:
  c+=b
  b+=1
print(f"the sum of natural number is : {c}")



a = int(input("Enter a number: "))
# range(1, a + 1) generates numbers from 1 to a
total_sum = sum(range(1, a + 1))
print(f"The sum of natural numbers is: {total_sum}")



# using for loop 
a = int(input("Enter a number : "))
b = 0
for i in range(1,a+1):
  b+=i
print(f"the sum of natural number is : {b}")
