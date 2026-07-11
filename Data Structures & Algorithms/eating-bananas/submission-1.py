from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low<high:
            mid = low + (high-low)//2
            feasible = sum(ceil(pile/mid) for pile in piles)
            if feasible <= h:
                high = mid
            else:
                low = mid+1    
        return low