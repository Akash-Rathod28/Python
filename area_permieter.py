import math
area1 = ["Rectangle","Square","Circle","Tria"
"ngle"]
user2 = input("Enter you want to claculate(Area/Perimeter:)").lower()
if user2 == "area":
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
elif user2 == "perimeter":
    
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
        perimeter = 2*(length+width)
        print(f"The Perimeter of Rectangle is {perimeter}")
    elif user == "circle":
        radius = float(input("Enter the radius:"))
        area = 2 * math.pi * radius
        print(f"The Perimeter of the circle is{area}")
    elif user == "triangle":
        side1 = float(input("Enter 1st side : "))
        side2 = float(input("Enter 2nd side : "))
        side3 = float(input("Enter 3rd side : "))
        perimeter = side1 + side2 + side3
        print(f"The Perimeter of the triangle is{perimeter}")
    elif user == "square":
        side1 = float(input("Enter 1st side : "))
        side2 = float(input("Enter 2nd side : "))
        side3 = float(input("Enter 3rd side : "))
        side4 = float(input("Enter 4th side : "))
        perimeter = side1 + side2 + side3 + side4
        print(f"The Perimeter of the Square is{perimeter}")
    else:
        print("Enter in area/perimeter like this" )
else:
    print("Enter area /rectangle")

