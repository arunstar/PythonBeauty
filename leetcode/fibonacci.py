
def fib(n):
    dp = [0] * (n +1)
    if n == 1  or n == 2:
        return 1
    elif n == 0:
        return 0
    dp[1] = 1
    dp [2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1 ]+ dp[i-2]
    print(dp)
    return dp[n]
print("Done",fib(4))