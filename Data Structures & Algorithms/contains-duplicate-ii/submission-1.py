from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        num=deque(nums[:k+1])
        
        if len(num)>len(set(num)):
            return True

        for i in range(len(nums)-k-1):
            num.popleft()
            num.append(nums[i+k+1])
            if len(num)>len(set(num)):
                return True
        
        return False

