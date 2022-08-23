class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = [len(nums2)-1]
        
        nextGreater = [0] * (len(nums2)-1) + [-1]
        
        for i in reversed(range(0,len(nums2)-1)):
            currElement = nums2[i]
            # we want to find next "greater element"
            while stack and nums2[stack[-1]] < currElement:
                stack.pop()
                
            nextGreater[i] = stack[-1] if stack else -1
                
            # insert this element
            stack.append(i)
            
            
        result = []
        for num in nums1:
            index = nums2.index(num)
            if nextGreater[index] == -1:
                result.append(-1)
                continue
            result.append(nums2[nextGreater[index]])
            
        return result
        