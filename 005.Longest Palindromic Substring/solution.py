class Solution(object):
    def longestPalindrome(self, s):
        res =''
        for i in range(len(s)):
            #Odd case i is in the center
            start = end = i
            while end<len(s) and start>=0 and s[start]==s[end]:
                start-=1;end+=1
            temp = s[start+1:end]
            
            if len(temp)>len(res):
                res=temp
                
            #Even case:
            start, end = i, i+1
            while end<len(s) and start>=0 and s[start]==s[end]:
                start-=1;end+=1
            temp = s[start+1:end]
            
            if len(temp)>len(res):
                res=temp
        return res
