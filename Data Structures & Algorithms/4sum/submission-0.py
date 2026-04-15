class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for j in range(len(nums)-3):

            if j > 0 and nums[j] == nums[j-1]:
                continue

            for i in range(j+1,len(nums)-2):
                
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                l=i+1
                r= len(nums)-1


                while l<r:
                    summ = nums[l]+nums[r]+nums[i]+nums[j]
                    if summ == target:
                        res.append([nums[j],nums[i],nums[l],nums[r],])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                            
                    if summ<target:
                        l+=1
                    if summ>target:
                        r-=1
        
        return res