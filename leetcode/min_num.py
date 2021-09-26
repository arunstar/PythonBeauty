
def find_min(n,nums):
    val = nums[0]
    for i in range(1,n):
        print("---",nums[i],val)
        if nums[i] < val:
            val = nums[i]
    return val

# n = int(input())
# nums = [int(i) for i in input().split(" ")]
# print(find_min(n,nums))

n = 5
nums = [100,1000,5,10000,3]
print(find_min(n,nums))