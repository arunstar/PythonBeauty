

def find_dup(nums):
    for i in range(len(nums)):
        print(nums)
        val = abs(nums[i])
        if nums[val] < 0:
            return val
        else:
            nums[val] = -nums[val]


def leet(nums):
    for num in nums:
        cur = abs(num)
        if nums[cur] < 0:
            return cur
        nums[cur] = -nums[cur]
        print(nums)
    
        
nums = [1,3,4,2,2]
#nums = [3,1,3,4,2]
#nums =  [2,2,2,2,2]
print("result",find_dup(nums))


# total = sum(nums) - sum(range(len(nums)))
# print(total)