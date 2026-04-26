class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        m=max(piles)
        res = m

        while l<=m:
            mid=(l+m)//2

            tt=0
            for p in piles:
                tt += math.ceil(float(p)/ mid)
            
            if tt<h:
                res=mid
                m=mid-1
            else:
                l=mid+1
            
        return res