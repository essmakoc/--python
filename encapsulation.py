class BankaAccount(object):
    def __init__(self, name, money, address):
        self.name = name
        self.__money = money
        self.address = address
        
    
    def getMoney(self):
        return self.__money
    def setMoney(self, amount):
        self.__money = amount
    def __increase(self):
        self.__money = self.__money + 500
   
        
   
    
p1 = BankaAccount("esma", 1000, "Ankara")
p2 = BankaAccount("yusuf", 2000, "Corum")

print("Get medhod: ",p1.getMoney())

p1.setMoney(5000)
print("after set method: ", p1.getMoney())

# p1.__increase()
# print("after raise: ", p1.getMoney())