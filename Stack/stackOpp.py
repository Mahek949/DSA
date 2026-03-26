class Stack:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)   
    #using append function
    
    def push(self,value):
        self.s.append(value)

    def peek(self):
        if len(self.s)==0:
            print("Stack is empty")
        else:
            return self.s[-1]
            
    def pop(self):
         if len(self.s)==0:
            print("Stack is empty")
         else:
             return self.s.pop()


stk=Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.s)
print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.pop())