import math
area1 = ["Rectangle","Square","Circle","Tria"
"ngle"]
u  = 1
i = 0
while i<len(area1):
    print(f"{u}.{area1[i]}")
    u += 1
    i+=1

user = input("Enter which are you want to calculate: ").lower()

if user == "rectangle":
    length = float(input("Enter the Length :"))
    width = float(input("Enter the width: "))
    area = length * width
    print(f"The Area of the Rectangle is{area}")
    
elif user == "square":
    side = float(input("Enter a side: "))
    area = math.pow(side,side)
    print(f"The Area of the square is{area}")

elif user == "circle":
    radius = float(input("Enter the radius:"))
    area = math.pi * math.pow(radius,radius)
    print(f"The Area of the circle is{area}")

elif user == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = ((1/2)*base*height)
    print(f"The Area of the traingle is{area}")

else:
    print("enter a valid area to find next tym..")
    
