class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
    
        
        #create a set with all cities that have an outgoing location
        outgoingCities = set()
        for i in range(len(paths)):
            outgoingCities.add(paths[i][0])
            
        #print unique cities (should have every single city in the 2d list)
        print(outgoingCities)
        
        
        #loop through all to-cities and if it isn't in outgoing then return that one
        for i in range(len(paths)):
            if paths[i][1] not in outgoingCities: 
                return paths[i][1]
        
            
        return None
                
                
                
#     [[london, newyork]
#      [ny, lima], 
#      [lima, sao paulo]]
                