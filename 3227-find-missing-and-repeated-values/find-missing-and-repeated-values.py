class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        l =[]
        n = len(grid)
        for i in range(0,n):
            for j in range(0,n):
                l.append(grid[i][j])
        
        for i in range(1,(n*n)+1):
            if l.count(i) == 2:
                arr.append(i)
            
        for i in range(1,(n*n)+1):
            if l.count(i) == 0:
                arr.append(i)
        return arr
            
        