######### PRIVATE AND PUBLIC
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # to make private use __ before the variable
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")
print(acc1.acc_no)# public outside the class
#print(acc1.__acc_pass)
print(acc1.reset_pass())


class Person:
    __name = "annoyms" # private __
    def __hello(self):
        print("HEllo World")
    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__hello)
# print(p1.__name)
print(p1.welcome())

