#parend 
class Animal:
    
    def __init__(self):
        print("animal is created")
    
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")

#child

class Monkey(Animal):
    
    def __init__(self):
        super().__init__()
        print("monkey is created")
        
    def toString(self):
        print("monkey")
    
    def climb(self):
        print("monkey can climb")
        


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def toString(self):
        print("brid")
    
    def fly(self):
        print("brid can fly")
  
    

m1 = Monkey()
m1.climb()
m1.walk()
m1.toString()




print("--------")
b1 = Bird()
b1.fly()
b1.walk()
