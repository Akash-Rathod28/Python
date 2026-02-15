a = int(input("Enter a Number:"))
b = 1
for i in range(1,a+1):
    b *= i
print("the factorial of the number is",b)

# another Way
import math
a = int(input("Enter a number to find fact"))
print(math.factorial(a))
