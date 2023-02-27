M = int(input())
N = int(input())
lst = []
chng = []
for _ in range(N):
    s = input()
    s = s.split()
    x = int(s[0])
    y = int(s[1])
    if lst:
        for index in range(len(lst)):
            lb = lst[index][0]
            rb = lst[index][1]
            if not((x<lb and y < lb) or (x>rb and y>rb)):
                chng.append(index)
        for ptr in chng[::-1]:
            lst.pop(ptr)
        chng = []
        lst.append([x,y])
            
    else:
        lst.append([x,y])
        
print(len(lst))