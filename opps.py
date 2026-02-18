class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def avg(self):
        avg = (self.mark1 + self.mark2 + self.mark3)/3
        return avg
s1 = Student("Akash Rathod",90,98,99)
print(s1.avg())


# another method
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        b = sum(self.marks)
        a = b/3
        print("hi",self.name,"Your avg score is :",a)
s1 = Student("Akash Rathod",[98,95,96])
s1.avg()     

# 3rd method
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        
        for val in self.marks:
            b = sum(self.marks)
            a = b/3
        print("hi",self.name,"Your avg score is :",a)
s1 = Student("Akash Rathod",[98,95,96])
s1.avg()

  


