class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        result = []
        i = 0
        j = 0
        k = 0
        flag = True
        while i < len(nums):
            if flag:
                result.append(a[j])
                j+=1
            else:
                result.append(b[k])
                k+=1
            i+=1
            flag = not flag
            
        return result
            
        