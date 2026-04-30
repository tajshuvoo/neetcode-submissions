class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        h=sum(weights)

        res=0

        while l<=h:
            mid= (l+h)//2

            count=1
            s=0
            i=0
            while i<=(len(weights)-1):
                s+=weights[i]
                if s>mid:
                    count+=1
                    s=weights[i]
                    i+=1
                else:
                    i+=1
                
            if count<=days:
                res=mid
                h=mid-1
            else:
                l=mid+1

        return res