
from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        print("I'm process abstract method of Computer class")
        pass

class Laptop():
    # __slots__ = ('x','y')
    def process(self):
        print("I'm process method of Laptop class")
        super().process()
        return None

a = Laptop()
# print(a.__dict__)
# a.name =  "Arun"
# a.process()
# print(type(a))

import sys
print(sys.getsizeof(dict()))
print(sys.getsizeof(tuple()))

class Base(object):
    def go(self):
        raise NotImplementedError("Please Implement this method")

class Specialized(Base):
    def go(self):
        print("OK")

s = Specialized()
print(s.go())
print(s.__init__)