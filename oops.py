class Parrot:

def __init__(self,name,age):
    self.name=name
    self.age=age

def sing(self,song):
    return "{} sings {} and his age is {}".foramt(self.name,self.age,song)

 def dance(self):
    return "{} singdance {} and his age is {}".foramt(self.name)

obj=Parrot("adnan",18)
print(obj.sing(" koye mil gaya"))
print(obj.dance)