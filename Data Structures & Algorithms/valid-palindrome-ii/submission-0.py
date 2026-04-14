class Solution:
    def validPalindrome(self, s: str) -> bool:
        hash={}
        for char in s:
            hash[char]= hash.get(char,0)+1
        count=0

        for key, val in hash.items():
            if val==1:
                count+=1
        
        return True if count==1 or count==0 else False