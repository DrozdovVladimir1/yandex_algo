str1 = ''
with open(r'D:\Desktop\input.txt', 'r') as file1:
    while True:
        tmp = file1.readline()
        if not tmp:
            break
        if '\n' in tmp:
            str1+=tmp[:-1]
        else:
            str1+=tmp
dict1 = {}
for char in str1:
    if char != ' ':
	    dict1[char] = dict1.get(char, 0) + 1
list1 = list(dict1.items())
list1 = sorted(list1, key=lambda x: ord(x[0]))
max_y = 0
for _,y in list1:
    max_y = max(max_y, y)
for i in range(max_y):
    for j in range(len(list1)):
        if max_y-i <= list1[j][1]:
            print('#', end='')
        else:
            print(' ', end='')
    print()
for x,_ in list1:
    print(x, end='')


