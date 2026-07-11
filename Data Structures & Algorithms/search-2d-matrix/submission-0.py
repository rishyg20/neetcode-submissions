class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0])-1 
        cols = len(matrix[0])
        while lo<=hi:
            mid = lo + (hi-lo)//2
            row = mid//cols
            col = mid%cols
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                lo = mid+1
            else:
                hi = mid-1    
        return False        

