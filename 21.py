N = int(input())
dp = [0]*(N+4)
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp[N])