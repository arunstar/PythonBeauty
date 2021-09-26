import timeit
mysetup = ""


# def input_to_dict(data):
#     a =dict(list(zip(aa[::2],aa[1::2])))
#     print(a)


# def input_to_dict2(data):
#     aa = ['id', '1', 'name', 'aru', 'age', '26']
#     a = {}
#     for i in range(1,len(aa),2):
#         a[aa[i-1]] = aa[i]

# aa = ['id', '1', 'name', 'aru', 'age', '26','ok']
# input_to_dict(aa)
# input_to_dict2(aa)

# print (timeit.timeit(setup = mysetup,
#                      stmt = m1,
#                      number = 100000000))

# print (timeit.timeit(setup = mysetup,
#                      stmt = m2,
#                      number = 100000000))

class Person():
    def __init__(self):
       pass
    
    def say_name(self,name):
        print(f'Hello my name is {name}')


class Employee(Person):

    def __init__(self,first,last):
        self.first = first
        self.last = last
        super().say_name(first+last)
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self,name):
        self.first,self.last = name.split(" ")

    @classmethod
    def from_string(cls,emp_string):
        first,last = emp_string.split(" ")
        return cls(first,last)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp = Employee.from_string("Arun M")
print(emp.email)
emp.email = "ok@email.com"

import datetime
dt = datetime.date(2021,9,3)
print(Employee.is_workday(dt))