
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or len(s) == 1:
            return len(s)

        n= len(s)
        hasht=[False]*256

        res=0
        l=0
        r=0

        while r<n:

            while hasht[ord(s[r])]==True:
                hasht[ord(s[l])]=False
                l+=1
            
            hasht[ord(s[r])]=True

            res= max(res, r-l+1)
            r+=1
        
        return res

