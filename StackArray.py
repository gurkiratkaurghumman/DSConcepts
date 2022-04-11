#STACK USING ARRAY

def createStack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item)

def pop(stack):
    if (isEmpty(stack)):
        return (maxsize-1)
    return stack.pop() #pop is array method like append

def peek(stack):
    if (isEmpty(stack)):
        return (maxsize -1) # return minus infinite
    return stack[len(stack) - 1]

stack = createStack()
maxsize=len(stack)
push(stack,10)
push(stack,20)
push(stack,30)
print(pop(stack))
print(stack)
