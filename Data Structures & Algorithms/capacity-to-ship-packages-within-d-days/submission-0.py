class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        h=sum(weights)

        res=0

        while l<=h:
            mid= (l+h)//2

            count=0
            s=0
            for i in range(len(weights)):
                s+=weights[i]
                if (s+weights[i])>mid:
                    count+=1
                    s=0
                
            if count<=days:
                res=mid
                h=mid-1
            else:
                l=mid+1

        return res