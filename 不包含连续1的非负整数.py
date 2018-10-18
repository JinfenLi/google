# coding=utf-8
# 给定一个正整数n，求出0到n中有几个数满足其二进制表示不包含连续的1。1<=n<=10^9。
# 举个例子，n=10，二进制为1010：
# 对于最高位的1，我们将0到1010分为0到111和1000到1010两部分，前一部分的个数为f(3) = 5。
# 第二部分为1000到1010，最高位确定取1，而n的二进制从左往右第二位为0，
# 为满足不超过n的条件，满足条件的数从左往右第二位只能取0。
# n的二进制从左往右第三位为1，这样我们又可以按i中的方法，把1000到1010再次分成1000到1001和1010两个部分，
# 前一部分的个数为f(1) = 2。 到n的最低位，为0，故最后一位只能取0，
# 按照之前的算法这一步不会增加答案，但由于n=1010b本身还没有计入，故再加1。最后得到答案5+2+1=8。
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 2:
            return num + 1

        str = bin(num).replace('0b', '')
        str = str[::-1]
        k = len(str)

        f = [0] * k
        f[0] = 1
        f[1] = 2
        #包含0,1情况
        for i in range(2, k):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        for i in range(k - 1, -1, -1):
            if str[i] == '1':
                ans += f[i]
                # 若两个连续1则返回
                if i < k - 1 and str[i + 1] == '1':
                    return ans
        ans += 1
        return ans
