# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        
        first = None
        second = head
        
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
            
        return first
        