class ST():
    def __init__(self):
        self.stk = []


    def push(self, n):
        self.stk.append(n)
        print('ok')

    def pop(self):
        if len(self.stk) == 0:
            print('error')
            return
        print(self.stk.pop())

    def back(self):
        if len(self.stk) == 0:
            print('error')
            return
        print(self.stk[-1])

    def clear(self):
        self.stk = []
        print('ok')

    def size(self):
        print(len(self.stk))

    def exit(self):
        print('bye')
tmp = ST()
s = input()
while (s != 'exit'):
    s = s.split()
    if s[0] == 'push':
        tmp.push(int(s[1]))
    if s[0] == 'size':
        tmp.size()
    if s[0] == 'back':
        tmp.back()
    if s[0] == 'pop':
        tmp.pop()
    if s[0] == 'clear':
        tmp.clear()
    s = input()
tmp.exit()