######## inheritance

# single Inheritance
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class ToyatoCar(Car):
    def __init__(self,name):
        self.name = name
    

car1 = ToyatoCar("Fortuner")
car2 = ToyatoCar("Prius")
print(car1.start(),car1.stop(),car1.color)


# multi level inheritance
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class ToyatoCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyatoCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("dieseil")
car1.start()
print(car1.type)

# multiple inheritance
class A:
    vara = "Welcome to class a"
class B:
    varb = "Welcome To class B"
class C(A,B):
    varc = "Welcome to class C"
c1 = C()
print(c1.vara)
print(c1.varb)
print(c1.varc)

### super method
class Car:
    def __init__(self,type):
        self.type = type

    
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class ToyatoCar(Car):
    def __init__(self,brand,type):
        super().__init__(type)
        self.brand = brand
        super().start()

car1 = ToyatoCar("Pirus","Electric")
print(car1.type)
