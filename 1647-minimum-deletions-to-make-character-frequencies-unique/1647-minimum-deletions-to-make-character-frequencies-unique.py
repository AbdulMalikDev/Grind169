class Solution:
    def minDeletions(self, s: str) -> int:
        
        nums = [0] * (len(s)+1)
        n = len(nums)
        result = 0
        running = 0
        freq = defaultdict(int)
        
        for char in s:
            freq[char] += 1
        freqToChar = defaultdict(int)
        for char,frequency in freq.items():
            nums[frequency] += 1
        print(freq)
        # pri
        while nums and nums[-1] == 0:
            nums.pop()
        print(nums)
        pointer = len(nums) - 1
        
        while pointer > 0:
            num = nums[pointer]
            if num == 0 and running > 0:
                running -= 1
            elif num > 1:
                running += (num-1)
                
            if running > 0:
                result += running
                
            
            pointer -= 1
            
        return result if result > 0 else 0
            
#         for num in nums:
            
#             if num == 0:
#                 result -= 1
#             elif num > 1:
#                 result += (num-1)
                
        
            
        
        