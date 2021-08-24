class WebSite:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        print(self.name + " " + self.surname)


class WebSite1(WebSite):
    def __init__(self, name, surname, ids):
        super().__init__(name, surname)
        self.ids = ids
        
    def loginInfo(self):
         print(self.name + " " + self.surname + " " + self.ids)



class WebSite2(WebSite):
    
    def __init__(self, name, surname, eposta):
        WebSite.__init__(self, name, surname)
        self.eposta = eposta
    
    def loginInfo(self):
         print(self.name + " " + self.surname + " " + self.eposta)

p1 = WebSite("name", "surname")

p1.loginInfo()  

p2 = WebSite1("esma", "koc", "123")
p2.loginInfo()

p3 = WebSite2("yusuf", "koc", "yusuf@gmail.com")
p3.loginInfo()