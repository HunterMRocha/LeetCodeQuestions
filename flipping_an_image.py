class Solution:
    def flipAndInvertImage(self, arr: List[List[int]]) -> List[List[int]]:
        
        #step 1: flip each array i.g [1,1,0] -> [0,1,1]
#         [1,1,0,1]
#         [1,0,1,0]
#         [0,0,0,1]
             
        for row in arr:
            row.reverse()
        # print(arr)
        
        #step 2: invert each array i.g [1,1,0] -> [0,0,1]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 1: 
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
        
        #step 3: return the newly updated arr that has been flipped and inverted
        return arr