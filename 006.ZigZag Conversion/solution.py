class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ['']*numRows
        if len(s)<=numRows:
            return s
        if numRows == 1:
            return s
        
        index, step = 0, 1
        
        for i in s:
            res[index] += i
            if index == 0:
                step =1    
            if index == numRows-1:
                step=-1
            index+=step
            
        return ''.join(res)
