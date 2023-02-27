s = input()
dict1 = {}
for index, char in enumerate(s):
    dict1[char] = dict1.get(char, 0) + (index+1) * (len(s) - index)
lst = list(dict1.items())
lst = sorted(lst, key=lambda x: ord(x[0]))
for key, value in lst:
    print(f"{key}: {value}")