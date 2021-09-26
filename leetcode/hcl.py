
# find only missing number
# constraints : no repetition and only one missing number
import profile

arr = [0,1,2,4]
print(arr)
print(sum(arr))

all_elements = list(range(len(arr)+1))
print(all_elements)
n= len(arr)
print(n* (n +1)//2)
print(sum(all_elements))

print(sum(all_elements) - sum(arr))
print("==========================")
# length = len(arr)

# for i in arr:
#     print(length - i)

# def find_missing(items):
#     for i in items:
#         if i not in arr:
#             return i


            


# print(all_elements)
# print(find_missing(all_elements))



matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9] ]

# [ [0,1,2]   [(0,0) (0,1) (0,2)]
#   [0,1,2]   [(1,0) (1,1) (1,2)]
#   [0,1,2]   [(2,0) (2,1) (2,2)]
# ]

# # op = [1,4,2,7,5,3,8,6,9]
# # pos = a[0] , a[1][]

d = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # print(i,j)
        key = i+j+1
        if key in d:
          d[key].append(matrix[i][j])
        else:
          d[key] = [matrix[i][j]]
print(d)

result = []

for key in d.keys():
  if key % 2 == 0:
    result.extend(d[key][::-1])
  else:
    result.extend(d[key])

print(result)