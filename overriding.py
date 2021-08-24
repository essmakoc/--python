class Animal: #parent
    
    def toString(self):
        print("Animal")
        
class Monkey(Animal):
    
    def toString(self):
        print("Monkey")
        
        
a1 = Animal()
a1.toString()

a2 = Monkey()
a2.toString() #Overriding 