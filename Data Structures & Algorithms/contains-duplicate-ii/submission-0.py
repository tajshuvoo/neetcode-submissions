from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        num=deque(nums[:k+1])
        
        if len(num)>len(set(num)):
            return True

        for i in range(len(nums)-k):
            num.popleft()
            num.append(nums[i])
            if len(num)>len(set(num)):
                return True
        
        return False

