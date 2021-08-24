from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def walk(self):
        pass
    @abstractclassmethod
    def run(self):
        pass


class Bird(Animal):
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk")
        
    def run(self):
        print("run")
    
b1 = Bird()