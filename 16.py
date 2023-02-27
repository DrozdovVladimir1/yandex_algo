from collections import deque
class DQ():
    def __init__(self):
        self.deque = deque()
    
    def push(self, n):
        self.deque.append(n)
        print('ok')

    def pop(self):
        if self.deque:
            print(self.deque.popleft())
        else:
            print('error')

    def front(self):
        if self.deque:
            print(self.deque[0])
        else:
            print('error')

    def size(self):
        print(len(self.deque))
    
    def clear(self):
        self.deque = deque()
        print('ok')

    def exit(self):
        print('bye')

deq = DQ()
s = input()
while (s!='exit'):
    tmp = s.split()
    if tmp[0] == 'push':
        deq.push(int(tmp[1]))
    elif tmp[0] == 'pop':
        deq.pop()
    elif tmp[0] == 'front':
        deq.front()
    elif tmp[0] == 'size':
        deq.size()
    elif tmp[0] == 'clear':
        deq.clear()
    s = input()
deq.exit()