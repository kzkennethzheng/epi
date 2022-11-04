import heapq

class stack:
    def __init__(self):
        self.a = []
        self.h = []
    
    def size(self):
        return len(self.a)

    def pop(self):
        x = self.a.pop()
        for i, y in enumerate(self.h):
            if x == -y:
                del(self.h[i])
                break
        heapq.heapify(self.h)
    
    def peek(self):
        return self.a[-1]

    def push(self, x):
        self.a.append(x)
        heapq.heappush(self.h, -x)

    def max_elmt(self):
        return -self.h[0]

class stack2:
    def __init__(self):
        self.a = []
        self.maxs = []

    def push(self, x):
        self.a.append(x)
        if self.maxs:
            self.maxs.append(max(x, self.maxs[-1]))
        else:
            self.maxs.append(x)

    def pop(self):
        self.maxs.pop()
        return self.a.pop()
    
    def max_elmt(self):
        return self.maxs[-1]

    def peek(self):
        return self.a[-1]

s = stack2()
a = [5, 7, 2, 1]
for x in a:
    s.push(x)
print(s.max_elmt(), s.peek())

s.pop()
s.pop()
s.pop()
print(s.max_elmt())
s.push(3)
print(s.max_elmt())
s.push(9)
print(s.max_elmt())