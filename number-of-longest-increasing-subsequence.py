# coding=utf-8
# 设f(i)表示L中以ai为末元素的最长递增子序列的长度。则有如下的递推方程：
# 这个递推方程的意思是，在求以ai为末元素的最长递增子序列时，
# 找到所有序号在L前面且小于ai的元素aj，即j<i且aj<ai。如果这样的元素存在，
# 那么对所有aj,都有一个以aj为末元素的最长递增子序列的长度f(j)，把其中最大的f(j)选出来，
# 那么f(i)就等于最大的f(j)加上1，即以ai为末元素的最长递增子序列，
# 等于以使f(j)最大的那个aj为末元素的递增子序列最末再加上ai；
# 如果这样的元素不存在，那么ai自身构成一个长度为1的以ai为末元素的递增子序列。
class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        #state and init
        f = [1] * len(nums)
        ans = [1] * len(nums)
        #func
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > f[i]:
                        #说明出现了新的序列
                        ans[i] = ans[j]
                        f[i] = f[j] + 1
                    #有序列长度一样就相加
                    elif f[j] + 1 == f[i]:
                        ans[i] += ans[j]
        #ans
        res = sum(y for x, y in zip(f, ans) if x == max(f))
        return res
s=Solution()
print s.findNumberOfLIS([1,3,5,4,7])