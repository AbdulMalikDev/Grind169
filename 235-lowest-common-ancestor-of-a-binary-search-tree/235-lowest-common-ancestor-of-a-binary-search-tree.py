# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, a, b):
        # If root itself is the LCA
        if root==a or root==b:
            return a if root==a else b
        
        # Since not given in question properly
        # I am ensuring that p is always the smaller value
        # and q is always the bigger one since we are using the
        # BST sorted property this matters to us
        p = a if a.val <= b.val else b
        q = b if p==a else a
        
        # Notice how you are given a Binary Search Tree
        # not just a Binary Tree
        # How can we use the properies of a BST for this problem?
        # well, we know that for a node to be the lowest common ancestor
        # in a BST, it has to be greater than p and smaller than q
        # along with handling some edge cases this is pretty much the solution
        
        while root:
            if p.val <= root.val <= q.val:
                return root
            
            elif root.val > q.val:
                root = root.left
                
            elif root.val < p.val:
                root = root.right
                
        
        