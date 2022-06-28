class Solution:
    def minDeletions(self, s: str) -> int:
        
        nums = [0] * (len(s)+1)
        n = len(nums)
        result = 0
        running = 0
        freq = defaultdict(int)
        
        for char in s:
            freq[char] += 1

        for char,frequency in freq.items():
            nums[frequency] += 1
            
        while nums and nums[-1] == 0:
            nums.pop()
            
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
            
        return result
            

                
        
            
        
        