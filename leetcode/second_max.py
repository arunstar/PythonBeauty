
def find_second_max(nums):
    n = len(nums)
    second_max = max_val =0
    for i in range(n):
        if nums[i] > max_val:
            second_max = max_val
            max_val = nums[i]
        elif nums[i] > second_max:
            second_max = nums[i]
    
    return {"max_val":max_val,"second_max":second_max}

arr = [1,3,2,7,5]
print(find_second_max(arr))