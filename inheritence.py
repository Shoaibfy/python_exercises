class Animal:
    def __init__(self):
        print("Animal created")
    def whoami(self):
         print("Animal")
    def eat(self):
         print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def whoami(self):
         print("Dog")
    def eat(self):
        print("Eating")

d=Dog()
d.whoami()
d.eat()

