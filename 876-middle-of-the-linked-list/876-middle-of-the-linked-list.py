# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        slow = head
        fast = head
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
            
            
        return slow
        