# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        if not list1 or not list2:
            return list1 or list2
        
        # You can imagine this solution like holding a sewing pin
        # and sewing together all nodes in a sorted fasion
        
        first = list1
        second = list2
        root = ListNode(1)
        result = root
        
        while first and second:
            
            if first.val <= second.val:
                root.next = first
                first = first.next
            else:
                root.next = second
                second = second.next
            root = root.next
                
        while first:
            root.next = first
            first = first.next
            root = root.next
        while second:
            root.next = second
            second = second.next
            root = root.next
            
            
        return result.next
            
                
                
            
        
        
        