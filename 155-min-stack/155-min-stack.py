class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        minVal = min(self.getMin(),val)
        self.stack.append((val,minVal))
        

    def pop(self):
        self.stack.pop()
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        if not self.stack:
            return sys.maxsize
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()