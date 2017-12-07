class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        if strs == []:
            return ''
        if '' in strs:
            return ''
        long_prefix = strs[0]
        length = len(strs[0])
        for i in range(1,len(strs)):
            if len(strs[i]) < length:
                long_prefix = long_prefix[:len(strs[i])]
                length = len(strs[i])
            while length >= 0 and strs[i][:length] != long_prefix:
                length -= 1
                long_prefix = long_prefix[:-1]
        if length == -1:
            return ''
        return long_prefix
