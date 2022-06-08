"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, node):
        
        if node is None:
            return 0
        
        maxDepth = 0
        for child in node.children:
            maxDepth = max(maxDepth,self.maxDepth(child))
        
        return maxDepth + 1
        