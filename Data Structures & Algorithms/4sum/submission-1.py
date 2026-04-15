class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for j in range(n - 3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue

            for i in range(j + 1, n - 2):
                # FIX: Check against i > j + 1, not i > 0
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue

                l = i + 1
                r = n - 1

                while l < r:
                    summ = nums[j] + nums[i] + nums[l] + nums[r]
                    if summ == target:
                        res.append([nums[j], nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif summ < target: # Use elif to avoid unnecessary checks
                        l += 1
                    else:
                        r -= 1
        
        return res