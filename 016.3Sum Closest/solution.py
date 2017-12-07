class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        close = abs(nums[0] + nums[1] + nums[len(nums)-1]-target)
        out = 0
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                
                if abs(s-target) <= close:
                    close = abs(s-target)
                    out = s
                
                if s == target:
                    return target            
                if s < target:
                    l +=1
                if s > target:
                    r-=1
        return out
                    
                
