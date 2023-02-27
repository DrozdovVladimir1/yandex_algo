N = int(input())
max_x = -9999999
max_y = -9999999
min_y = 9999999
min_x = 9999999
for _ in range(N):
    s = input()
    s = s.split()
    x,y = s
    x = int(x)
    y = int(y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)
print(f"{min_x} {min_y} {max_x} {max_y}")