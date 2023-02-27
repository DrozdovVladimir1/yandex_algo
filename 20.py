x = input()
lst= []
y = input()
y = y.split()
for elem in y:
	lst.append(int(elem))
y = sorted(y)
for elem in y:
	print(elem, end=' ')