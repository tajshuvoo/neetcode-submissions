class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        table={}

        cnt= len(nums)//3
        num=[]
        for i in range(len(nums)):
            table[nums[i]] = table.get(nums[i],0)+1
            if table[nums[i]]>cnt:
                num.append(nums[i])

        return list(set(num))