class Employee():
    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = '{}.{}@gmail.com'.format(first,last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        self.first,self.last = name.split(' ')
        

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    

emp = Employee('Arun','Murugesan')
emp.first = 'Aroon'
print(emp.first)
print(emp.last)
print(emp.fullname)
print(emp.email)
emp.fullname = 'Spider Man'
print(emp.email)