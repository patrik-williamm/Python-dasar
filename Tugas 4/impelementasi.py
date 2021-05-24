
class Stack():
	def init(self):
		self.top = None
		self.size = 0
		pass

def isEmpety(self):
	return self.items == []
	pass

def push(self, item):
	self.items.append(item)
	pass

def pop(self):
	return self.item.pop()
	pass

def peek(self):
	return self.items[len(self.item)-1]
	pass

def size(self):
	return len(self.items)
	pass

s=Stack()
s.push('patrik')
s.push('william')

print(s.isEmpety())
print(s.peek())

while not(s.isEmpety()):
	print(s.pop())


