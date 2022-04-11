'''
enQueue(q, x): 

While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q): 

If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)
'''

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enqueue(self,item):
        while(len(self.s1)!=0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(item)
        while(len(self.s2)!=0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def dequeue(self):
        if(len(self.s1)==0):
            print("queue empty")
        item=self.s1[-1]
        self.s1.pop()
        return item
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())

print(q.dequeue())
print(q.dequeue())


'''OUTPUT
1
2
3'''

