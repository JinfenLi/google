# coding=utf-8
import sys


def maximumaveragesubarrayii(nums, k):
    n = len(nums)
    l = sys.maxint
    r = -2147483648
    # l为最小元素，r为最大元素
    for i in range(n):
        l = min(l, float(nums[i]))
        r = max(r, float(nums[i]))
    sumNums = [0] * (n + 1)
    # sumNums储存前i个元素的总和-i*A,即 s(i)=b(0)+b(1)+……+b(i-1)
    sumNums[0] = 0
    while r - l > 1e-6:
        # 平均数在变化
        mid = float((l + r)) / 2
        # s(i)=b(0)+b(1)+……+b(i-1)
        for i in range(n):
            sumNums[i + 1] = sumNums[i] + nums[i] - mid
        preMin = 0.0
        sumMax = -2147483648
        # b(j)到b(i-1)的区间和可表示为s(i)-s(j)
        for i in range(k, n + 1):
            # 满足i-j>=k，且使s(i)-s(j)最大
            sumMax = max(sumMax, sumNums[i] - preMin)
            # 则要使s(i)-s(j)最大，s(j)应最小
            preMin = min(preMin, sumNums[i - k + 1])
        # 使得其平均值大于等于A，即(a(i)+a(i+1)+……+a(i+L-1))/L >= A，
        # 那么我们所求的答案应当大于等于A；反之如果对于所有长度大于等于k的子数组，
        # 其平均值均小于A，那么我们所求的答案也必然小于A。
        if sumMax >= 0:
            l = mid
        else:
            r = mid
    return r


print maximumaveragesubarrayii([1, 12, -5, -6, 50, 3], k=4)
