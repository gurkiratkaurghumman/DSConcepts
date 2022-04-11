'''
enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).
Here time complexity will be O(1)

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Here time complexity will be O(n)
'''

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,item):
        self.s1.append(item)
    def dequeue(self):
        # if both empty return empty queue
        # if only s1 has elements then push everything to s2 by popping the elements one by one from s1 and repeat till s1 is empty
        ## else return last element of s2 
        if len(self.s1)==0 and  len(self.s2)==0:
            print("queue empty")
            
        elif len(self.s1)>0 and  len(self.s2)==0:
            while len(self.s1)!=0:
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()
q=Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

'''
OUTPUT
1
2
3
queue empty
None
'''