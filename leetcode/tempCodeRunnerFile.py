if 1 <= val <= len(nums) :
            if nums[val-1] > 0:
                nums[val-1] = -1 * nums[val-1]
            elif nums[i] == 0:
                nums[val-1] = -1 * (len(nums) +1)