N = int(input())
K = int(input())
x = int(input())
y = int(input())
tmp = 2*x +(y-2)
x1 = (tmp+K+1)//2
x2 = (tmp-K+1)//2

x1_diff= abs(x-x1)
x2_diff = abs(x-x2)
if (tmp+K <=N)and(x1_diff <=x2_diff):
    if K %2 != 0:
        if y == 1:
            y = 2
        else:
            y = 1
    print((tmp+K+1 )//2 )
    print(y)
elif (tmp-K>0):
    if K %2 != 0:
        if y == 1:
            y = 2
        else:
            y = 1
    print((tmp - K+1)//2 )
    print(y)
else:
    print(-1)


