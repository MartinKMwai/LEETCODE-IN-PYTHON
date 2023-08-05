class MinStack:

    def __init__(self):
        #create two stacks
        self.stack=[]
        self.minStack = []
        

    def push(self, val: int):
        #append the value into our stack
        self.stack.append(val)
        #check our new value and see how it compares to the current least number in or min stack
        val = min (val, self.minStack[-1] if self.minStack else val)
        #append our new minimum value to the stack
        self.minStack.append(val)
        

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()