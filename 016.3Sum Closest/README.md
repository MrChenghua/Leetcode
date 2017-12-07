思路和3sum基本一致，同样对列表进行排序后，遍历list。取得index i 后，向后取两个指针一个在i+1，一个位于len(nums)-1。
为了取出重复值，当 i>0 and nums[i]==nums[i-1]时，i += 1;continous。
计算三个数的和s，定义close = abs(s-target)。如果close != min(abs(s-target),close)，更新close为 abs(s-target),将result赋值为s。

当s == target 时，直接输出target。
当s < target时，左指针加一：l += 1。
当s > target时，右指针减一：r -= 1。（因为list已经进行过排序）

两指针遍历的条件是：l<r。同时为了去除重复计算，当发现nums[l]==nums[l+1]时，l += 1；nums[r]==nums[r-1]时，r -= 1。
