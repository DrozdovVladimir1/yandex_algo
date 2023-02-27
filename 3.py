def searchInsert(nums, target):
    if target < nums[0]:
        return 0
    if target > nums[len(nums)-1]:
        return len(nums)
    a = 0
    b = len(nums)-1
    c = a+b //2
    while (b-a > 1):
        if (target > nums[c]):
            a = c
        else:
            b = c
        c = (a+b)//2
    if (nums[a] == target):
        return a
    return b
N = int(input())
clct = []
tmp = input()
tmp = tmp.split()
for elem in tmp:
    clct.append(int(elem))
clct = list(set(clct))
clct = sorted(clct)
K = int(input())
if N == 0:
    for _ in range(K):
        print(0)
lst = []
tmp = input()
tmp = tmp.split()
for elem in tmp:
    elem = int(elem)
    x = searchInsert(clct, elem)
    print(x)

