
# Kadane's Algorithm
def find_max_sum(nums):
    prev_sum = max_sum = nums[0]
    for i in range(1,len(nums)):
        cur_val = nums[i]
        prev_value = nums[i-1]
        if cur_val > prev_value:
            prev_sum = max(cur_val,cur_val + prev_sum)
        if prev_sum > max_sum:
            max_sum = prev_sum
    return max_sum

arr = [-2,3,2,-10,1,2,3]
# print(find_max_sum(arr))

import snoop

@snoop
def longest_increasing(nums):
    max_length = 1
    cur_length = 1
    prev = nums[0]
    for i in range(1,len(nums)):
        
        if nums[i] > prev:
            print(nums[i],prev)
            cur_length += 1
        else:
            cur_length = 1
        
        if cur_length > max_length:
            max_length = cur_length
        prev = nums[i]
    print("Done")
    return max_length

nums = [1,2,3,1,1,1,2,3,4,5]
print(longest_increasing(nums))