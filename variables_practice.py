#1
num = 25
print(num)

#2
a,b = 10,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#3
name = input("Enter your name:")
age = int(input("Enter your age: "))
print(f'My name is {name} and my age is {age}')

#4
a,b,c,d = 9,"akash",95.5,True
print(type(a))
print(type(c))
print(type(b))
print(type(d))

#5
x =5
y = 8
x,y = y,x
print(x,y)

# another method to swap
x = x+y
y = x-y
x = x-y
print(x,y)

#6
x = "10"
y = 5
print(int(x)*y)
print(x*5)

#7
a = int(input("enter a:"))
b = int(input("enter b:"))
print(a+b)
print(a*b)

#8
a = int(input("enter a number:"))
c = float(a)
d = str(c)
print(f"a ={a} ,c = {c},d = {d},{type(a)}")

# 9
a = True 
b = False
print(a+b)
print(a*5)
print(b+10)

#10
user = input("enter a number:")
if "." in user:
    print(type(float(user)))
else:
    print(type(int(user)))


#11(5*2+3)
output : 13

#12
a,b =10,a
print(a+b)

#13

print(5 == 5)
print(5 == "5")
print(5 is 5)
print(5 is "5")

#14
nums = [1,2,3]
nums.append(4)
print(nums)

#15
user = input("enter a name")
print(user)
print(type(user))

