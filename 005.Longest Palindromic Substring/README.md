遍历字符串，对奇数、偶数分开处理：

回文字符为奇数：
在循环中，取每个index为中心。分别向index左右去遍历，看是否s[i-step]和s[i+step]相等。需满足的条件是：i-step>=0, i+step<len(s)。

为偶数：
需要比对是的s[i]与s[i+1]两边的字符是否相等，即判断s[i-step]==s[i+1+step]。

在截取回文字符串：s[i-step+1:i+step]，并保存最长的字符串。
