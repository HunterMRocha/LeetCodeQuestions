class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #create a dict that contains each value with its index
        map = {}
        for i in range(len(nums)):
            map[i] = nums[i]
            
            
        #create a var that hold that difference between the target and current nums[i]
        for i in range(len(nums)):
            complement = target - nums[i]
            print('comp', complement)
            if complement in map.values() and complement != i: 
                for idx, val in map.items(): 
                    if val == complement and idx != i:
                        return (i, idx)
                
        return None
        