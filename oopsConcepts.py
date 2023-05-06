#class is a onkect constructor / blueprint for crating objects

#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("janvi",19)

print(p1.name,p1.age)

#or representation with a __str__()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"


p1=person("janvi",19)

print(p1)