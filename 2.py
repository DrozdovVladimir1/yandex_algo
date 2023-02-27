k = int(input())
s = input()
dict1 = {}
l, r = 0,0
maxChar = 0
ans = max(k, 1)
for r in range(len(s)):
    char1 = s[r]
    if char1 not in dict1:
        dict1[char1] = 1
    else:
        dict1[char1]+= 1
    maxChar = max(maxChar, dict1[char1])
    if (r-l +1 -maxChar > k):
        dict1[s[l]] -=1
        l+=1
    ans = max(ans, r-l+1)
print(ans)