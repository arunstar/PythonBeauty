
# ip = [5,3,4,1,2]
# op = 2

from collections import defaultdict

def find(n,nums):
    for i in range(n):
        print(nums[:i+1],nums[i+1:])


def sumOfElements(arr, n) :
 
    # dictionary is used to store
    # element frequencies
    m = dict.fromkeys(arr, 0)
 
    for i in range(n) :
            m[arr[i]] += 1
 
    print(m)
    ok = 0
 
    # traverse the dictionary
    for key,value in m.items() :
 
        # Calculate the sum of elements
        # having frequencies greater than
        # or equal to the element itself
        if value >= key :
                ok += key
 
    return ok

n = 5
nums = [1,2,3,4]

print(sumOfElements(nums,n))