
class Employee():

    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = '{}.{}@email.com'.format(first,last)
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        return int(self.pay * self.raise_amt) 


class Developer(Employee): 
    pass

dev1 = Employee('Arun','M',10000)
dev2 = Developer('Raghav','M',10000)
print(dev1.email)
print(dev1.apply_raise())
