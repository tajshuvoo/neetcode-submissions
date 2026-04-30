class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)

        while l<h:
            m=(l+h)//2
            if nums[m]==target:
                return m
            elif nums[m]>nums[h-1]:
                l=m+1
            else:
                h=m

        return -1