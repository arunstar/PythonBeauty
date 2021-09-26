def find_missing(nums):
    """
    :type nums: List[int]
    :rtype: int
        Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
    """
    print(nums,len(nums))
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): # delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    print(nums)
    for i in range(len(nums)): # use the index as the hash to record the frequency of each number
        nums[nums[i]%n]= nums[nums[i]%n] + n
    print(nums)
    for i in range(1,len(nums)):
        print(nums[i],n)
        if nums[i]/n==0:
            return i
    return n


def neet(A):
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0
    print("after step 1",A)
    for i in range(len(A)):
        print("after step 2",A)
        val = abs(A[i])
        if 1 <= val <= len(A):
            if A[val - 1] > 0:
                A[val -1 ] *= -1
            elif A[val -1] == 0:
                A[val -1] = -1 * (len(A) + 1)
    
        
    for i in range(1,len(A)+1):
        if A[i-1] >=0:
            return i
    return len(A) +  1


def arun(nums):

    for i in range(len(nums)):
        if nums[i] < 0 :
            nums[i] = 0
    print(nums)
    print("="*30)

    for i in range(len(nums)):
        val = abs(nums[i])
        print(val)
        if 1 <= val <= len(nums) :
            if nums[val-1] > 0:
                nums[val-1] = -1 * nums[val-1]
            elif nums[i] == 0:
                nums[val-1] = -1 * (len(nums) +1)
        print(nums)
    
    for i in range(len(nums)):
        if nums[i] >= 0:
            return i + 1
    return len(nums) + 1

# nums = [7,8,9,11,12]
nums = [1,2,0]
#nums = [3,4,-1,1]
#nums = [1]
# nums = [-2,-3,-4,-5,0]
nums = [0,1,2]
print(neet(nums))