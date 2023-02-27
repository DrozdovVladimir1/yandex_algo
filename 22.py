# s = input()
# s=s.split()
# N = int(s[0])
# k = int(s[1])
# k = min(k, N)
# if (N == k):
#     N+=1
# dp = [0]*(N)
# for i in range(1,k+1):
#     dp[i] = sum(dp[:i]) +1
# for i in range(k+1, N):
#     dp[i] = sum(dp[i-k:i])
# print(dp[-1])
    
s = input()
s=s.split()
N = int(s[0])
k = int(s[1])
if (N<=k):
	print(2**(max(0,N-2)))
else:
    k = min(k, N)
    if (N == k):
        N+=1
    dp = [0]*(N)
    for i in range(1,k+1):
        dp[i] = sum(dp[:i]) +1
    for i in range(k+1, N):
        dp[i] = sum(dp[i-k:i])
    print(dp[-1])
