这个问题有两个解法：利用循环来求解或者利用递归

方法一：

首先需要创建一个字典：dic = {'0':' ','1':' ','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
并定义results =[]。

遍历digits中每一个digit，随后定义一个temp的空列表用于写入字母。
遍历results中的每一个结果后，遍历digit所对应的dic[digit]中的字母letter，将result+letter传入到temp列表中，更新results = temp。

返回results。

方法二，利用递归来求解：

同样创立字典，以及results = []。如果输入digits为空则返回空。随后构建了递归函数dfs，需要传入的参数为digits，result以及results。初始result=''。

进入递归函数dfs，遍历dic[digits[0]]中的字母，对每个letter调用dfs如下，dfs(digits[1:],result+letter,results)。
当满足len(digits) == 0时，说明已将数字遍历完了，将result添加到results中。

该递归函数的空间复杂度较高，可以利用指针遍历降低其空间复杂度：
即定义dfs(dict,index,result,results),初始为dfs[digits,0,'',results]。
随后传入函数中，遍历dic[digits[index]]中的字母，随后调用迭代方程dfs(digits,index+1,result+letter,results)
当index==len(digits)时，说明已将数字遍历完了，将result添加到results中，results.append(result)。
