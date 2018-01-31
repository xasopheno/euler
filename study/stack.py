class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
s.push('hello')
print(s.items == ['hello'])

print(s.pop() == 'hello')

print(s.is_empty()==True)
s.push('hello')
print(s.is_empty()==False)

print(s.size() == 1)
s.push('False')
print(s.size() == 2)
