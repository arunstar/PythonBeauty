class foo(object):
	x = "original class"

print(foo.x)

c1 , c2 , c3= foo() , foo(), foo()
c1.x = "changed instance c1"
c3.x = "changed instance c3"
print(c1.x)

foo.x = "changed class"
print(foo.x)

print("=========")

print(c1.x)
print(c2.x)
print(c3.x)