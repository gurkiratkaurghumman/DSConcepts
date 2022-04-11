'''enQueue(x)
  1) Push x to stack1.

deQueue:
  1) If stack1 is empty then error.
  2) If stack1 has only one element then return it.
  3) Recursively pop everything from the stack1, store the popped item 
    in a variable res,  push the res back to stack1 and return res
        '''

class Queue:
	def __init__(self):
		self.s = []
		
	
	def enQueue(self, data):
		self.s.append(data)
	
	def deQueue(self):
		
		if len(self.s) <= 0:
			print('Queue is empty')
			return
		
	
		x = self.s[-1]
		self.s.pop()
		
		if len(self.s) <= 0:
			return x
			
		item = self.deQueue() #recursive call
		self.s.append(x)
		return item
	
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
	
'''OUTPUT
2
2
3'''
