    # coding=utf-8

    # 对n个数的序列，a1，a2，……，an，判断是否存在i<j<k，使得ai<ak<aj（这样的[ai,aj,ak]被称为132模式）。n不超过15000。
    # 样例1
    # 输入： [1,2,3,4]
    # 输出： False
    # 样例3
    # 输入： [-1,3,2,0]
    # 输出： True
    # 说明： [-1,3,2]，[-1,3,0]，[-1,2,0]均为132模式
    # 令min(j)为a(1)，a(2)，……，a(j)中的最小值，那么如果[a(i),a(j),a(k)]为一个132模式，
    # 则[min(j-1),a(j),a(k)]也必为132模式，反之，如果[min(j-1),a(j),a(k)]不是132模式，
    # 那么对于任意i<j，[a(i),a(j),a(k)]都不会是132模式。
    # 令max(j)为a(j+1)，a(j+2)，……，a(n)中小于a(j)的最大值，那么a(k)即可用max(j)代替。
    # 与方法2中不同的是，此处要求的不是a(j)以后的数中的最大值，而是要小于a(j)的最大值，
    # 得到max(j)后，判断是否有min(j-1)<max(j)，如果成立则存在132模式，否则继续向前枚举j，
    # 如果对于所有的j均不成立，则不存在132模式。这样，时间复杂度为O(n)。
    # 从后往前枚举i，同时维护一组键值对{a(k),ans(k)}，ans(k)表示满足i<j<k且a(j)>a(k)的组数，
    # 故a(i)对答案的贡献为所有大于a(i)的a(k)对应的ans(k)之和；加入a(i)后，
    # 则将对所有小于a(i)的a(k)对应的ans(k)增加1，同时增加一组键值对{a(i),0}。
    import sys
    class Solution(object):
        def find132pattern(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            n = len(nums)
            if n <= 2:
                return False

            minPre = [0] * n
            minPre[0] = nums[0]
            # minPre[i]表示前i个数中的最小值
            for i in range(1, n):
                minPre[i] = min(minPre[i - 1], nums[i])

            maxStack = []
            for j in range(n - 1, 0, -1):
                max = -sys.maxint
                while len(maxStack) > 0 and maxStack[-1] < nums[j]:
                    max = maxStack.pop()
                if minPre[j - 1] < max:
                    return True
                maxStack.append(nums[j])
            return False