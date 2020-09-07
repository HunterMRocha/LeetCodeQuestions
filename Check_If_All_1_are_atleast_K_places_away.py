class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        #loop through and when we find a '1' loop through k times and if a 1 doesn't appear after k more iterations then return true
        
        for i in range(len(nums)): 
            if nums[i] == 1: 
                count = 1
                while(count <= k and i+count < len(nums)):                    
                    if  nums[i+count] == 1:
                        return False
                    else: 
                        count = count + 1
        return True
        