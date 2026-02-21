#1
class Employee:
    def __init__(self,role,debt,salary):
        self.role = role
        self.debt = debt
        self.salary = salary


    def showdetails(self):
        print("role =",self.role)
        print("debt =",self.debt)
        print("Salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")
# e1 = Employee("Accountant","Finance","60")
# e1.showdetails()

e1 = Engineer("Akash Rathod",40)
e1.showdetails()

#2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self, ordr2):
        return self.price > odr2.price
odr1 = Order("chips",20)
odr2 = Order("tea",15)

print(odr1 > odr2)
