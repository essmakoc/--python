from abc import ABC, abstractmethod

class Shape(ABC):
    # super class, abstractclass
   
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimater(self ):
        pass
    
    #overriding
    def toString(self):
        pass
      
#child
class Square(Shape):
    "sub class"
    def __init__(self, edge):
        self.__edge = edge
    
    def area(self):
        result = self.__edge**2
        print("Square area: ",result)   
  
    def perimater(self ):
        result = self.__edge*4
        print("Square perimater: ",result) 
     
    def toString(self):
        print("Square edge: ", self.__edge)
        
        
class Circle(Shape):
    
    PI = 3.14
    
    def __init__(self, r):
        self.__r = r
    
    def area(self):
        result = self.PI * self.__r ** 2
        print("Circle area: ",result)   
  
    def perimater(self):
        result = 2 * self.PI * self.__r
        print("Circle perimater: ",result) 
      
    def toString(self):
         
        print("Circle r: ", self.__r)   
      
        
   
c = Circle(5)    
c.area()
c.perimater()
c.toString() 
      
        
      
        
      
        