class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        nums = [0] * k
        result = sys.maxsize
        
        def distribute(cookies,index,nums,n):
            nonlocal result
            if index == n:
                result = min(result,max(nums))
                return
            
            if max(nums) > result:
                return 
            
            for i in range(k):
                # print(index)
                nums[i] += cookies[index]
                distribute(cookies,index+1,nums,n)
                nums[i] -= cookies[index]
            
            
            
        
        distribute(cookies,0,nums,n)
        return result
        