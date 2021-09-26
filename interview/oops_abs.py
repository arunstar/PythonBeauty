
from abc import ABC,abstractmethod

class Computer(ABC):

    age = 10
    @abstractmethod
    def process(self):
        print("I'm process abstract method of Computer class")
        pass

class Laptop(Computer):
    # __slots__ = ('x','y')
    pass


a = Laptop()
print(a.__dict__)
a.name =  "Arun"
a.process()
print(type(a))


# import sys
# print(sys.getsizeof(dict()))
# print(sys.getsizeof(tuple()))

# class Base(object):
#     def go(self):
#         raise NotImplementedError("Please Implement this method")

# class Specialized(Base):
#     pass
#     # def go(self):
#     #     print("OK")

# s = Specialized()
# print(s.go())
# print(s.__init__)