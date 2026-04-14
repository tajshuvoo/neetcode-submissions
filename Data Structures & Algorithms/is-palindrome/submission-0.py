class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned= "".join(char for char in s if char.isalnum())
        reverse = cleaned[::-1]
        return cleaned.lower()==reverse.lower()