import weakref
import oops

class Car():
    def __init__(self,wheels):
        self.wheels = wheels

    def getWheels(self):
        return self.wheels


c1 = Car(4)
print("c1 memory location ",hex(id(c1)))
r = weakref.ref(c1)
print("Weakref before ",r)
c1 = None
print("Weakref after ",r)
print(c1.getWheels())

print(oops.c1)


