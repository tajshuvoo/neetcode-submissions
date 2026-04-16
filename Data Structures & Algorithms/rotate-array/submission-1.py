class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(nums,k):

            nums.reverse()
            nums[0:k] = nums[0:k][::-1]
            nums[k:]= nums[k:][::-1]
        
        reverse(nums,k)