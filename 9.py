s = input()
s = s.split()
N,M,K = s
N = int(N)
M = int(M)
K = int(K)
lst = []
for _ in range(N):
    tmp = input()
    tmp = tmp.split()
    lst.append(tmp)
for i in range(N):
    for j in range(M):
        lst[i][j] = int(lst[i][j])
ans = []
for _ in range(K):
    s = input()
    s = s.split()
    x1,y1,x2,y2 = s
    x1 = int(x1)-1
    y1 = int(y1)-1
    x2 = int(x2)-1
    y2 = int(y2)-1
    sums = 0
    for i in range(x1, x2+1, 1):
            sums+=sum(lst[i][y1:y2+1])
    ans.append(sums)
for elem in ans:
    print(elem)   

