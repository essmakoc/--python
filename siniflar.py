
#

int1 = 33
str1 = "ali"

#%% classes

employee1_name = "messi"
employee1_age = 33
employee1_address = "Ankara"

class Employee(object):
    #özelikler = yas, adres, isim
    #davranislar = topAt, kos
    
    pass

employee1 = Employee()
#%% attribute

class Footballer:
    
    football_club = "barcelona"
    age = 30
    
f1 = Footballer()
    
print("yasi:", f1.age)

f1.football_club = "real madrid"
print(f1.football_club)

#%% methods

class Square(object):
    edge = 5
    
    def area(self):
        self.area = self.edge * self.edge
        
        print("Area:", self.area)

s1 = Square()


s1.area()


#%% methods and fonk

class Emp(object):
    age = 25
    salary = 1000
    
    def ageSalaryRatio(self):
        a =  self.age / self.salary
        print("method:", a)

e1 = Emp()
e1.ageSalaryRatio()

#-------------------

def ageSalaryRatio(age, salary):
    a = age / salary
    print("function:", a)


ageSalaryRatio(10, 10000)

#☺**********

def findArea(pi, r):
    area = pi*r**2
    #print(area)
    return area

pi = 3.14
r = 5

result1 = findArea(pi, r)
result2 = findArea(pi, 10)

print(result1 + result2)

#%% contructor

class Animal(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
    
a1 = Animal("dog",2)
a1.age = a1.getAge()

print("animal age:", a1.age)


a2 = Animal("cat", 5)
print(a2.getAge())

print(a2.getName())