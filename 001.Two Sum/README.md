回国第一个面试就遇到这个题，之前没有好好刷算法，二重循环求解的。估计凶多吉少了，现在开始刷起！

在讨论区看到的解法：
先创建一个空字典，把target与nums数字的差值作为目录，index作为内容, 依次传入。在下次向字典中传入数据前，先判别新数字是否在字典内。
如果存在于字典内，则直接输出两数指针。如果不在字典内，则将新数字于target的差值传入字典，继续迭代。
