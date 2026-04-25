class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue

                start, end = j+1, len(nums)-1
                while start<end:
                    total = nums[i]+nums[j]+nums[start]+nums[end]
                    if total==target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        while start<end and nums[start]==nums[start+1]:
                            start+=1
                        while start<end and nums[end]==nums[end-1]:
                            end-=1
                        start+=1
                        end-=1
                    elif total>target:
                        end-=1
                    else:
                        start+=1
        return res