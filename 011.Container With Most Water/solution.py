class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height)-1
        contain = 0
        while l < r :
            h = min(height[l],height[r])
            w = r-l
            contain = max(contain,h*w)
            if (height[l] < height[r]):
                l+=1
            else:
                r-=1
        return contain
