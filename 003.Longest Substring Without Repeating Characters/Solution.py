class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxlength = 0
        used_char = {} 
        for i,c in enumerate(s):
            if (c in used_char) and (start<=used_char[c]):
                start = used_char[c]+1
            else:
                maxlength = max(maxlength,i-start+1)
            used_char[c] = i
        return maxlength
