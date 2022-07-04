class A:
    def one(self):
        return self.two()
 
    def two(self):
        return 'A'
 
class B(A):
    def two(self):
        return 'B'
obj1=A()
obj2=B()
print(obj1.two(),obj2.two())

class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

class Dog:
     def walk(self):
         return "*walking*"
 
     def speak(self):
         return "Woof!"
 
class JackRussellTerrier(Dog):
     def speak(self):
         return "Arff!"
 
bobo = JackRussellTerrier()
bobo.speak()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
class JackRussellTerrier(Dog):
    pass
 
class Dachshund(Dog):
    pass
 
class Bulldog(Dog):
    pass
 
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)