# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def checkPalindrome(node,head):
            if node == None:
                return [True,head]
        
            result,head = checkPalindrome(node.next,head)
            
            if not result or node.val != head.val:
                return [False,None]
            # if head.next == node:
            #     return True
            return [True,head.next]
    
        print(checkPalindrome(head,head))
        return checkPalindrome(head,head)[0]