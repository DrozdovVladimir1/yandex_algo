stack = []
N = int(input())
s = input()
s = s.split()
next = 1
for elem in s:
    tmp = int(elem)
    if not (stack):
        stack.append(tmp)
    else:
        while stack and (stack[-1] == next):
            next+=1
            stack.pop()
        stack.append(tmp)
while stack and (stack[-1] == next):
    next+=1
    stack.pop()
if stack:
    print('NO')
else:
    print('YES')
        