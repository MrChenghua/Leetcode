class Solution(object):
    def letterCombinations(self,digits):
        maps = {'0':' ','1':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        if len(digits)==0:
            return []
        self.dfs(digits, maps, '', result)
        return result

    def dfs(self,digits, maps, sub, res):
        if len(digits)==0:
            res.append(sub)
        else:     
            for j in maps[digits[0]]:
                self.dfs(digits[1:], maps, sub+j, res)    
            
