# coding=utf-8
#  给定一个只包含正整数的非空数组，判断该数组能否分成两个和相等的子数组
# dp[i][j] = 1表示前i个元素能够得到和为j的子数组，dp[i][j] = 0 表示不能得到。那么对于第i个元素来说，有两种情况，一种是第i个元素在和为j的子数组中，那么对于前i-1个元素来讲，应该得到和为j-nums[i]的子数组；另一种情况是第i个元素不在和为j的子数组中，那么对于前i-1个元素来讲，应该得到和为j的子数组。
def canpartition(nums):
    length = len(nums)
    sum = 0
    for i in range(length):
        sum += nums[i]
    if sum % 2 == 1:
        return False
    sum /= 2
    dp = [False]*20000
    dp[0] = True
    for i in range(length):
        for j in range(sum,nums[i]-1,-1):
            dp[j] |= dp[j-nums[i]]
    return dp[sum]
print canpartition([1,2,3,5])