class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        count =0
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if s[l+1]==s[r]:
                    count+=1
                    l+=1
                elif s[l]==s[r-1]:
                    count+=1
                    r-=1
                else:
                    return False
        return True if count<=1 else False