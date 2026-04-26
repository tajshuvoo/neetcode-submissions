class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matt = [item for sublist in matrix for item in sublist]

        l=0
        h=len(matt)-1

        while l<=h:

            m=(h+l)//2

            if matt[m]==target:
                return True
            elif matt[m]>target:
                h=m-1
            else: l=m+1
        
        return False