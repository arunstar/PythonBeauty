def missingNumber(nums):
    n = len(nums)
    l = list(range(len(arr)+1))
    print(">>>>>>>>",sum(l))
    print(n ,"*", (n+1) ,"//", 2 ,"-",sum(nums))
    return (n * (n+1)) // 2 - sum(nums)

arr = [0,1,3,4,5]
print(missingNumber(arr))
print("w"*30)
print(100 * 101 // 2 == sum([i for i in range(101)]))