class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maxIndex = nums[::-1].index(max(nums))
        maxIndex = (n-1) - maxIndex
        # print(maxIndex)
        nums2 = nums[maxIndex+1:] + nums[:maxIndex+1]
        print(nums2)
        # O(N) Space
        stack = [nums2[-1]]
        
        nextGreater = defaultdict(int)
        nextGreater[(nums2[-1],len(nums)-1)] = -1
        
        # O(N) Time
        for i in reversed(range(0,len(nums2)-1)):
            currElement = nums2[i]
            # we want to find next "greater element"
            while stack and stack[-1] <= currElement:
                stack.pop()
                
            nextGreater[(currElement,i)] = stack[-1] if stack else -1
                
            # insert this element
            stack.append(currElement)
            
            
        result = []
        # O(M) Time
        for index,num in enumerate(nums2):
            result.append(nextGreater[(num,index)])
        
        reconcile = (n-2) - maxIndex
        print(nextGreater)
        print(result)
        return result[reconcile+1:] + result[:reconcile+1]
        
        