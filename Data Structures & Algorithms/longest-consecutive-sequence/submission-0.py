class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        sorted_unique= sorted(unique)

        count=1
        maximum=0

        for i in range(1,len(sorted_unique)):
            if sorted_unique[i]-sorted_unique[i-1] == 1:
                count+=1
                if count>maximum:
                    maximum= count
            else:
                count=1
        
        return maximum

