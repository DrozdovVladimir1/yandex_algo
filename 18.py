from collections import deque
class D:
    def __init__(self):
        self.dq = deque()
    def push_front(self, n):
        self.dq.append(n)
        print('ok')
    def push_back(self, n):
        self.dq.appendleft(n)
        print('ok')
    def pop_front(self):
        if self.dq:
            print(self.dq.pop())
        else:
            print('error')
    def pop_back(self):
        if self.dq:
            print(self.dq.popleft())
        else:
            print('error') 
    def front(self):
        if self.dq:
            print(self.dq[-1])
        else:
            print('error') 
    def back(self):
        if self.dq:
            print(self.dq[0])
        else:
            print('error')   
    def size(self):
        print(len(self.dq))
    def clear(self):
        self.dq = deque()
        print('ok')
    def exit(self):
        print('bye')
ameba = D()

s = input()
while (s!='exit'):
    tmp = s.split()
    if tmp[0] == 'push_front':
        ameba.push_front(tmp[1])
    elif tmp[0] == 'push_back':
        ameba.push_back(tmp[1])
    elif tmp[0] == 'pop_front':
        ameba.pop_front()
    elif tmp[0] == 'pop_back':
        ameba.pop_back()
    elif tmp[0] == 'front':
        ameba.front()
    elif tmp[0] == 'back':
        ameba.back()
    elif tmp[0] == 'size':
        ameba.size()
    elif tmp[0] == 'clear':
        ameba.clear()
    s = input()
ameba.exit()