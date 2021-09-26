def factorial(n):
    print(n)
    if n == 0:
        return 1
    return n * factorial(n-1)
num = 5
print("Factorial of", num, "is",factorial(num))

fact = 1
for i in range(2,5+1):
    fact = fact * i

print(fact)
print("Done")