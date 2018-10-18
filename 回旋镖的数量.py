# coding=utf-8
# 给出二维平面中的不同的N个点，找出回旋镖三元组的数量。
# 一个三元组(A,B,C)，如果满足点A到点B的距离等于点A到点C的距离，则被称为回旋镖。
# 同样三个点，不同顺序的三元组算不同的三元组。
# N<=500，所有点的坐标值为整数且都在[-10000,10000]中。
# 对于一个点A来说，如果有k个点到A的距离相等，那么就可以形成k*(k-1)个回旋镖
# （在k个点中任意选取两个不同的点均可以和A形成回旋镖，且不同的顺序算不同的方案）。
# 计算所有其他点到A点的距离，统计离A点有某个相同距离d的点有几个，最后将所有个数代入k*(k-1)并相加，
# 就得到了所有以A点为三元组中第一个点的回旋镖个数。

class Solution(object):
    def getDistance(self, a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx * dx + dy * dy

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points == None:
            return 0
        ans = 0
        for i in range(len(points)):
            disCount = {}
            for j in range(len(points)):
                if i == j:
                    continue
                distance = self.getDistance(points[i], points[j])
                count = disCount.get(distance, 0)
                disCount[distance] = count + 1
            for distance in disCount:
                ans += disCount[distance] * (disCount[distance] - 1)
        return ans