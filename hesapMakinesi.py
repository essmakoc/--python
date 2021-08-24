class Calc(object):
    
    #init metodu
    def __init__(self, a ,b):
        self.value1 = a
        self.value2 = b
        
        
    def add(self):
        return(self.value1 + self.value2)
        
    
    def multiply(self):
        return(self.value1 * self.value2)
        
     
    def division(self):
        return(self.value1 / self.value2)
    
c1 = Calc(5, 2)
print("Add: {}, Multiply: {}" .format(c1.add(), c1.multiply()))


print("Toplama (1), Carpma(2), Bolme(3) seciniz")
selection = input("select 1, 2, 3")

v1 = int(input("birinci sayi: "))
v2 = int(input("ikinci sayi: "))

c1 = Calc(v1, v2)

if selection == "1":
    print("Toplam: ", c1.add())
    
elif selection == "2" :
    print("Carpma: ", c1.multiply())
    
elif selection == "3":
    print("Bolme: ", c1.division())
    
else: 
    print("Yanlis secim!!!")