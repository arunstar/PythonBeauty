# class A:
#   def method(self):
#     print("A.method() called")

# class B:
#   def method(self):
#     print("B.method() called")

# class C(A, B):
#   pass

# class D():
#     def method(self):
#         print("No1")
#     def method(self):
#         print("No2")
#     def method(self):
#         print("No3")

# d = D()
# d.method()
# d.method()


# def foo(*args):
#     print(args)

# foo([1,2,3,4,5])



# def my_gen():
#     yield 5
#     for i in "arun":
#         yield i
#         print("I'm running")

# g = my_gen()
# print(next(g))
# print(next(g))
# print(next(g))


names = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

# print(dict(sorted(names.items())))
d = sorted(names.items(), key=lambda x: x[1])
# print(dict(d))

with open('/Users/arun/Projects/PythonBeauty/sample_log.txt','r') as f:
    # print(f.read())
    for chunk in f.read(100000):
        print(chunk)
        print("***********************")