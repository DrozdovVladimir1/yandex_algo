s = input()
s = s.split()
list1 = [int(i) for i in s]
s = input()
s = s.split()
list2 = [int(i) for i in s]
for i in range (1000000):
    if len(list1) == 0:
        print(f"second {i}")
        break
    if len(list2) == 0:
        print(f"first {i}")
        break
    x = list1[0]
    y = list2[0]
    if (x > y)and ((x!= 9) or (y!=0)) or x==0 and y==9:
        list2.pop(0)
        list1.pop(0)
        list1.append(x)
        list1.append(y)
    elif (x < y)and((y!=9)or(x!=0)) or x==9 and y==0:
        list1.pop(0)
        list2.pop(0)
        list2.append(x)
        list2.append(y)
if len(list1) != 0 and len(list2) !=0:
    print('botva')
