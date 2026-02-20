class Person:
    name = "anonymous"
    
    #def changename(self,name):
        # #self.name = name
        # #Person.name = name # to change the name of class atrribute
        # self.__class__.name = name

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("Rahul kumar")
print(p1.name)
print(Person.name)
