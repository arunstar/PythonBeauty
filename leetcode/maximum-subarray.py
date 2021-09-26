

# Solution 1 : Brute force : Worst solution
class Solution:
    sum_list = []
    def maxSubArray1(self, nums):
        count = 0
        sum_list = []
        for i in range(0,len(nums)):
            sum_list.append(nums[i])
            for j in range(i+1,len(nums)):
                count = count +1
                sum_list.append(sum(nums[i:j+1]))
        print(sum_list)
        print("n is {} , Took {} iteration(s)".format(len(nums),count))
        return max(sum_list)
    
    # Dynamic Programming O(n)
    def maxSubArray(self,nums):
        dp = [0]*len(nums)
        for i,num in enumerate(nums):
            if dp[i-1] + num > num:
                # dp[i] = max(dp[i-1] + num, num)
                dp[i] = dp[i-1] + num
            else:
                dp[i] = num
            # print(dp[i-1] , num)
            print(dp)
        return max(dp)

def test():
    sol = Solution()
    assert sol.maxSubArray([-2,1]) == 1
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5,4,-1,7,8]) == 23
    assert sol.maxSubArray([-2,1]) == 1
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

sol = Solution()
a = sol.maxSubArray([2,3,1,-7,9,8,7])
print("a ",a)
