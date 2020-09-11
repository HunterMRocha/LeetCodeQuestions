class Solution:
    def findContentChildren(self, kids: List[int], greed: List[int]) -> int:
        happy_kids = 0
        kids.sort()
        greed.sort()
        
        
        i = len(kids)-1
        j = len(greed)-1
        while j >= 0 and i >= 0: 
            if kids[i] <= greed[j]: 
                happy_kids += 1
                i -= 1
                j -= 1
            else: 
                i -= 1
            
        return happy_kids