class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # N -> no.of elements in nums2
        # M -> no.of elements in nums1
        
        # O(N) Space
        stack = [nums2[-1]]
        
        nextGreater = defaultdict(int)
        nextGreater[nums2[-1]] = -1
        
        # O(N) Time
        for i in reversed(range(0,len(nums2)-1)):
            currElement = nums2[i]
            # we want to find next "greater element"
            while stack and stack[-1] < currElement:
                stack.pop()
                
            nextGreater[currElement] = stack[-1] if stack else -1
                
            # insert this element
            stack.append(currElement)
            
            
        result = []
        # O(M) Time
        for num in nums1:
            result.append(nextGreater[num])
            
        return result
        