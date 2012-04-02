#Extend the stack with an additional operation called "minimum" which will return the minimum element stored in the stack. The "minimum" operation should be #implemented in O(1) time (that is, constant time. Note that this is the key requirement of the new design. Finding the minimum should be an operation which takes #the same amount of time irrespective of the number of elements in the stack. Sorting, scanning through a list using builtin functions (or your own code) etc are #things which are NOT O(1) - so they are not allowed).

class stack:
	def __init__(self):
		self.top=-1
		self.max=10
		self.list=[]
		self.dic={}
		self.min=0
	def push(self,data):
		if(self.top == self.max-1):
			print "Stack Overflow"
			return 0
		else:
			self.top+=1
			self.list.append(data)
			if len(self.dic)==0:
				self.dic[self.min]=data	
			elif data < self.dic[self.min]:
				self.min+=1
				self.dic[self.min]=data
	def pop(self):
		if (self.top == -1):
			print 'An exception, "IndexError", because stack is now empty'
			return 0
		else:
			num=self.list[-1]
			self.list=self.list[0:-1]
			self.top-=1
			if num == self.dic[self.min]:
				self.min -=1
			return num

	def minimum(self):
         	try: print self.dic[self.min]
                except : 
			print "Stack is empty"
			self.dic={}

a=stack()
a.push(10)
a.minimum()
a.push(20)
a.minimum()
a.push(9)
a.minimum()
a.pop()
a.minimum()
a.pop()
a.minimum()
a.pop()
a.minimum()
a.pop()
a.push(33)
a.minimum()
a.push(12)
a.minimum()
a.pop()
a.minimum()
