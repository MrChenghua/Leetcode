创建两个指针分别指向字符串的两端 l = 0;r = len(height)-1。容积的高 h = min(height[l],height[r])，宽 w = j-i，容积contain = w*h。
保存初始的contain，当 height[l] <= height[r]，将左指针加一，l += 1，否则 r -= 1。需要满足l < r。

计算新的宽与高，令contain == max(contain,w*h)。

