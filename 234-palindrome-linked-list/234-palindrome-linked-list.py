# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def checkPalindrome(self,node,head):
            if node == None:
                return [True,head]
        
            result,head = self.checkPalindrome(node.next,head)
            
            if not result or node.val != head.val:
                return [False,None]
            
            return [True,head.next]
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.checkPalindrome(head,head)[0]