class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for sublist in matrix:
        
            if sublist[0]<=target and sublist[len(sublist)-1]>=target:

                l=0
                h=len(sublist)-1

                while l<=h:

                    m=(h+l)//2

                    if sublist[m]==target:
                        return True
                    elif sublist[m]>target:
                        h=m-1
                    else: l=m+1
            
        return False