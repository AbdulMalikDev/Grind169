class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        # print(self.s1)

    def pop(self) -> int:
        if len(self.s2)==0:
            self.s2 = list(reversed(self.s1))
            # print(self.s2)
            self.s1 = []
        
        return self.s2.pop()

    def peek(self) -> int:
        if len(self.s2)==0:
            self.s2 = list(reversed(self.s1))
            self.s1 = []
            # print(self.s2)
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) == 0 and len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()