
class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack()
s.push('a')
print(s.is_empty())
print(s.peek())
print(s.is_empty())
print(s.pop())
print(s.is_empty())