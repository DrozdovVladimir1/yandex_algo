from collections import deque
s = input().split()
N = int(s[0])
M = int(s[1])
graph = [[0 for x in range(N)] for y in range(N)] 
x0 = None
y0 = None
for _ in range(M):
    tmp = input().split()
    x = int(tmp[0])-1
    y = int(tmp[1])-1
    graph[x][y] = 1
    graph[y][x] = 1
max_tmp = 1
visited = [0]*N
#path = f'{x0+1} '
path = ''
#max_path = f'{x0+1} ' 
max_path = ''
# def dfs(node, path, k=0):
#     global max_tmp
#     global max_path
#     for i in range(N):
#         if graph[node][i] == 1 and not visited[i]:
#             visited[i] = 1
#             dfs(i,path+f'{i+1} ',k+1)
#             visited[i] = 0
#     if max_tmp <= k:
#         max_path = path
#         max_tmp = k
path = '1 '
k = 1
dq = deque()
dq.append(0)
while (dq):
    node = dq.popleft()
    visited[node] = 1
    for i in range(N):
        if graph[node][i] == 1 and visited[i] == 0 and i not in dq:
            dq.append(i)
            k+=1
            path = path + f'{i+1} '
if M:
    #dfs(1, path)
    print(sum(visited))
    for index, value in enumerate(visited):
        if value:
            print(index+1, end=' ')
else:
    print(1)
    print(1)

