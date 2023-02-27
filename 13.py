stack = []
s = input()
s = s.split()
oper = '+-*'
for ch in s:
    if ch not in oper:
        stack.append(int(ch))
    else:
        a = stack.pop()
        b = stack.pop()
        if ch == '+':
            stack.append(int(b+a))
        elif ch == '-':
            stack.append(int(b-a))
        elif ch =='*':
            stack.append(int(b*a))
print(stack[0])
