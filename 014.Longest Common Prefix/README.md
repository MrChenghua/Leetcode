设置初始 prefix==strs[0]，prefix_long = len(strs[0])。

遍历list中的每一个字符串。当len(strs[i])<len(prefix)，将prefix_long赋值为len(strs[i])，prefix = prefix[:len(strs[i])]。

当prefix_long>0时，判断str[i][:prefix_long]与prefix是否相等。如果不等prefix_long -= 1，prefix_long = prefix_long[:-1], 继续迭代判断。

最终输出prefix。
