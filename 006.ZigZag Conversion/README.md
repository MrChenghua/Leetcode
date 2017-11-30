将字符排列成“之”字，并按行输出。如果numRows==1或者len(s)<numRows，直接输出s。

初始化输出列表为res = ['']*numRows，这里用到的巧妙的用到了index和step。遍历字符串s时，将相同index的字符传入res[index]中：res[index]+=s[i]

随着字符串的遍历，index随着步幅改变：index+=step。当index==0时，step =1，当index == numRows-1时，step变为-1。
