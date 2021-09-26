
def beautify(func):
    def inner(*args,**kwargs):
        print("*************")
        func(*args,**kwargs)
        print("*************")
    return inner

def say_hello():
    print("Hello")

say_hello = beautify(say_hello) # same as # @beautify
say_hello()
print()