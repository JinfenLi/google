#coding=utf-8
import sys
class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def numberofarithmeticslices(self,A):
        if A is None or len(A)<3:
            return 0
        map = []
        ans = 0
        for i in range(len(A)):

            map.append({})
            for j in range(i):
                if abs(long(A[i])-A[j])>sys.maxint:
                    continue
                d = A[i] -A[j]
                # if d not in map[i]:
                #     map_i_d = 0
                # else:
                #     map_i_d = map[i][d]
                if d not in map[j]:
                    map_j_d = 0
                else:
                    map_j_d = map[j][d]
                # 同时由于（A(k),A(j)）长度为2，不计入g(j,k)的中，但（A(k),A(j),A(i)）应计入g(i,j)中，
                # 故将g(j,k)计算入g(i,j)时还要额外加1。
                # 我们令f(i,d)表示以A(i)结尾，公差为d的等差子序列的个数，这里我们允许存在长度为2的等差子序列
                map[i][d] = map_j_d+1
                # 第一次只有两个元素，所以ans=0
                ans += map_j_d
        return ans
s = Solution()
print s.numberofarithmeticslices([2, 4, 6, 8, 10])