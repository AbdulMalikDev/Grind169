class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = self.right=None
        
    def insert(self,node):
        
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        elif self.end <= node.start:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        else:
            return False
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start,end)
            return True
        return self.root.insert(Node(start,end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)