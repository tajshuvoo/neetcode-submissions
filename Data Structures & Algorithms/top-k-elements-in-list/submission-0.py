class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash=[0]*(abs(max(nums)-min(nums))+1)
        minimum=min(nums)
        for i in range(len(nums)):
            hash[nums[i]-minimum]=hash[nums[i]-minimum]+1
        
        result=[]
        for i in range(k):
            maximum= max(hash)
            number = hash.index(maximum)
            hash[number] = 0
            result.append(number+minimum)
        
        return result

