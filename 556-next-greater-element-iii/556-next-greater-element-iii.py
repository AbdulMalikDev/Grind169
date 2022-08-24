class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        num = n
        nums2 = []
        while num!=0:
            nums2.insert(0,num%10)
            num = num//10
        lengthOfNums2 = len(nums2)
        
        pivot = -1
        # find decreasing suffix
        for i in reversed(range(len(nums2)-1)):
            currElement = nums2[i]
            nextElement = nums2[i+1]
            
            if currElement < nextElement:
                pivot = i
                break
        
        # already maximum as whole is decreasing
        if pivot == -1:
            return -1
                
        # replace pivot with next greater
        toReplace = -1
        number = sys.maxsize
        for i in range(pivot+1,len(nums2)):
            if nums2[i] > nums2[pivot] and nums2[i] <= number:
                toReplace = i
                number = nums2[i]
        nums2[pivot],nums2[toReplace] = nums2[toReplace],nums2[pivot]
        
        
        # reverse the rest of the array
        nums2 = nums2[:pivot+1] + list(reversed(nums2[pivot+1:]))
        result = int("".join(map(str,nums2))) 
        return result if result <= 2147483647 else -1 
        
        
        
        
#         stack = [nums2[-1]]
        
#         nextGreater = defaultdict(int)
#         nextGreater[(nums2[-1],len(nums2)-1)] = -1
        
#         # O(N) Time
#         for i in reversed(range(0,len(nums2)-1)):
#             currElement = nums2[i]
#             # we want to find next "greater element"
#             while stack and stack[-1] <= currElement:
#                 stack.pop()
                
#             nextGreater[(currElement,i)] = stack[-1] if stack else -1
                
#             # insert this element
#             stack.append(currElement)
            
            
#         result = []
#         for index,num in enumerate(nums2):
#             result.append(nextGreater[(num,index)])
        
#         if not any(x!=-1 for x in result):
#             return -1
#         print(nums2)

#         for i in reversed(range(len(result))):
#             if result[i] != -1:
#                 nextGreater = nums2[::-1].index(result[i])
#                 nextGreater = lengthOfNums2 - nextGreater - 1
#                 atPresentNum = i
#                 nums2[nextGreater],nums2[i] = nums2[i],nums2[nextGreater]
#                 nums2 = nums2[:i+1] + list(reversed(nums2[i+1:]))
#                 break
        
#         print(result)
#         resultNum = int(''.join(map(str,nums2))) 
#         return resultNum if resultNum <= ((2**32)-1) else -1 
        