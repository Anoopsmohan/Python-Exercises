#Using a "class", create a simple "Stack" data structure in Python. It should work like this:

class stack:
	def __init__(self):
		self.top=-1
		self.max=10
		self.list=[]
	def push(self,data):
		if(self.top == self.max-1):
			print "Stack Overflow"
			return 0
		else:
			self.top+=1
			self.list.append(data)


	def pop(self):
		if (self.top == -1):
			print 'An exception, "IndexError", because stack is now empty'
			return 0
		else:
			num=self.list[-1]
			self.list=self.list[0:-1]
			self.top-=1
			return num
	def is_empty(self):
		if self.top==-1:
         		return True
		else:
			return False

a=stack()
a.push(10)
a.push(20)
i=a.pop()
print i
i=a.pop()
print i
i=a.pop()
k=a.is_empty()
print k

