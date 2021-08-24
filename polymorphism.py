class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee: ", result)
        
class Ce(Employee):
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("Ce: ", result)
  
class Eee(Employee):
    
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("Eee: ", result)

    
    
e1 = Employee()

ce = Ce()

eee = Eee()

e1.raisee()
ce.raisee()
eee.raisee()

print("-----------")

employee_list = [ce, eee]

for employee in employee_list:
    employee.raisee()