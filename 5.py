N = int(input())
lst = []
for i in range(N):
    tmp = input()
    lst.append( int(tmp) )
ans = 0
i = 0
while (True):
    l,r = 0, 0
    while(l < len(lst)-1 and lst[l] == 0):
        l+=1
    if l == len(lst)-1:
        break
    if l != len(lst) and lst[l+1] == 0:
        lst[l] = 0
        continue
    r = l+1
    while (r < len(lst)-1 and lst[r+1] !=0):
        r+=1
    x = min(lst[l:r+1])
    for i in range(l, r+1):
        lst[i]-=x
    ans+= x * (r-l)
print(ans)

