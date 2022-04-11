# STACK USING lINKED LIST



class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.elements=[None]*maxsize
        self.top=-1

    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    def isFull(self):
        if self.top==self.maxsize-1:
            return True
        return False

    def push(self,data):
        if (self.isFull()):
            print("stack full")
        else:
            self.top=self.top+1
            self.elements[self.top]=data

    def pop(self):
        if self.top==-1:
            print("stack empty")
        else:
            data=self.elements[self.top]
            self.top=self.top-1
            return data
    
    def display(self):
        if(self.isEmpty()):
            print("empty")
        index=self.top
        print("top to down")
        while(index>=0):
            print(self.elements[index])
            index-=1
        
stack=Stack(10)
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(3)
stack.pop()
stack.push(5)
stack.display()


OUTPUT

top to down
5
4
2
1
