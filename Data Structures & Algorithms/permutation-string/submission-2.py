class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def checkf(s1h:list[int], s2h:list[int])->bool:
            for i in range(len(s1h)):
                if s1h[i]!=s2h[i]:
                    return False
            
            return True
        
        k=len(s1)
        s1h=[0]*26
        s2h=[0]*26
        for i in range(len(s1)):
            s1h[ord(s1[i])-ord('a')]+=1
            s2h[ord(s2[i])-ord('a')]+=1
        

        for i in range(len(s2)-k+1):
            if checkf(s1h,s2h):
                return True
            if i+k<len(s2):
                s2h[ord(s2[i+k])-ord('a')]+=1
                s2h[ord(s2[i])-ord('a')]-=1
        
        return False