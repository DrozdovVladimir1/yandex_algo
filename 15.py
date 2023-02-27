N = int(input())
s = input()
s=s.split()
stack = []
ans = []
for index in range(len(s)-1, -1, -1):
    e = int(s[index])
    while (stack and int(s[stack[-1]]) >= e):
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(index)
ans = ans[::-1]
for elem in ans:
    print(elem, end=' ')
    
