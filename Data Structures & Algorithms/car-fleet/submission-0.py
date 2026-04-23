class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[]
        both=list(zip(position,speed))
        sort_both= sorted(both, key=lambda x: x[0] , reverse =True)

        for pos,spe in both:

            time= (target-pos)/spe
            if len(s)==0:
                s.append(time)
                continue
            
            if time>s[-1]:
                s.append(time)
        
        return len(s)


