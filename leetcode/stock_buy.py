# from typing import List

# # class Solution:
# #     def maxProfit(self, prices: List[int]) -> int:
# #         min_value = min(prices)
# #         max_value = max(prices)
# #         index_of_min = prices.index(min_value)
# #         index_of_max = prices.index(max_value)
# #         if  index_of_max > index_of_min:
# #             return prices[index_of_max]
# #         else:
# #             return 0

# # prices = [7,1,5,3,6,4]
# # sol = Solution()
# # print(sol.maxProfit(prices))


# # def do(l):
# #     a = l
# #     print(id(a))
# #     print(id(l))
# #     a.append(6)

# # l = [1,2,3,4,5]
# # do(l)
# # print(l)

# # [].append(3)

# def armstrongNumber():
# 	# Write your code here
#     arr = [153,108,12]
#     for num in arr:
#         result = 0
#         newNum = num
#         while(newNum):
#             # print(num)
#             rem = newNum % 10
#             # print(rem)
#             result = result + rem ** 3
#             newNum = newNum // 10
#         # print(result,num)
#         if result == num:
#             print("It is an ARMSTRONG number")
#         else:
#             print("It is NOT an ARMSTRONG number")

# a = armstrongNumber()
# print(a)


# def my_func(n, i, j):
#   a, b = n.index(i), n.index(j)
#   return a, b


# n = [2, 4, 8, 10, 8, 12]
# i = 8
# j = 1

# if __name__ == "__main__": 
#   a, b = my_func(n, i, j)
#   print(a, b)


# num = 4

# def foo(num):
#   return num**3

# print(foo(3)**2)

# def foo():
#   x = 'Python'
#   def bar():
#     nonlocal x
#     x = 'Java'
#   bar() 
#   return x

# print(foo())

n=3
A=[[i for i in range(n)] for i in range(n)]
print(A)

num1 = 0
def out_func():
  num1 = 1
  def in_func():
    global num1
    num1 = 2

  in_func()
  return num1

num2 = out_func()
print(num1, num2)