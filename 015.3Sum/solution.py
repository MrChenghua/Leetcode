class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s==0:
                    result.append(nums[i],nums[l],nums[r])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and num[r]==num[r-1]:
                        r-=1
                    l+=1;r-=1
                if s<0:
                    l+=1
                if s>0:
                    r-=1
        return res
                
