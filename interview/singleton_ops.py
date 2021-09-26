
def singleton(class_):
    instances = {}
    def getinstace(*args,**kwargs):
        if class_ not in instances:
            print("calling")
            instances[class_] = class_(*args,**kwargs)
        print("Done")
        return instances[class_]
    return getinstace
    

@singleton
class A():
    pass

a = A()
b = A()