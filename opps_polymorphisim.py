#polomorphism

### ------IMPLICIT OVERLOADING ALREADY DONE BY THE PYTHON
print(1+2)# addition
print("Apna" + "college") # concatining
print([1,2,3,4] + [5,6,7]) #merging the list

###----- OPERATING OVERLOADING
class Complex:
    def __init__(self,real,img):
        self.img = img
        self.real = real

    def showNumber(self):
        print(self.real,"i +",self.img,"j")


    #def add(self,num2):
    def __add__(self, num2): #dunder function __add__
        newreal  = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)
    def __sub__(self, num2): #dunder function __subraction__
        newreal  = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal,newimg)
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()

# num3 = num1 + num2
# # num3 = num1.add(num2)
# print("______________")
# num3.showNumber()

num3 = num1 - num2
#num3 = num1.add(num2)
# print("______________")
num3.showNumber()


