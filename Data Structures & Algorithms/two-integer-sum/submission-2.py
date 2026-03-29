class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]== target and i!=j:
                    idx.append(i)
                    idx.append(j)
                    break
            if len(idx)>0:
                break

        return idx