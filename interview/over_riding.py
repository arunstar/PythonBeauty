class A(object):
    def foo(self):
        print ('A.foo()')

class B(object):
    def foo(self):
        print ('B.foo()')

class C(A, B):

    hike = 5
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def raise_hike(cls,hike_val):
        cls.hike =  hike_val

    @classmethod
    def from_string(cls,emp_str):
        fname,lname = emp_str.split("-")
        return cls(fname,lname)
    
c = C("Arun","Murugesan") 
f = c.from_string("John-Cena")
print(f)
c.raise_hike(100)
print(C.hike)
r = C("K","R")
print(r.hike)

import datetime as dt
from typing import Any
print(dt.date.today() + dt.timedelta(days=1))

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

# @singleton
class MyClass():
    def __init__(self):
        print("")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return "Honey"

a = MyClass()
b = MyClass()

print(a())
print(a is b)

def filter_logic(x):
    return x % 2 ==0

list_new  = list(filter(filter_logic, [1,2,3,4,5,6,7]))
print(list_new)


print("------------------------------")

class Base():
    def __init__(self):
        self.a = "arun"

    def get_name(self):
        Base.__init__
        return self.name

class Derive(Base):
    def __init__(self):
        print("Calling protected member of base class: ")
        print(self.a)

# d = Derive()
# print(d.a)

class Foo():
    a = 777
    _a = 777
    __a = 777

foo = Foo()
print(Foo.__dict__)


from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from copy import copy,deepcopy

l = [1,2,3,[4,5]]
l3 = deepcopy(l)
l[3].append(6)
print(l)
print(l3)

from datetime import datetime
x = datetime.now()
print(x.strftime("%Y"))

dt = datetime.strptime("05 09, 2021","%d %m, %Y")
print("OKkkkk",dt.day)

def demo(l):
    a = l
    a = []
    a.append(5)
    return a

l = [2,3,4,5]
print(l)
print(demo(l))
print(l)

import unittest

# class TestString(unittest.TestCase):
    
#     def test_upper(self):
#         self.assertEqual('foo'.upper(),'FOO')

# unittest.main()

c = 1

def add():
    return c + 1
print(add())