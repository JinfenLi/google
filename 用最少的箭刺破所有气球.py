#coding=utf-8
#  一个气球的横向直径两端横坐标为xbegin,xend，一支箭射击的横坐标为x，
# 如果有xbegin<=x<=xend，则这支箭可以刺破该气球。没有箭的使用数量限制，并且一支箭可以刺破相应坐标上的所有气球。
# 求出刺破所有气球所需的最少的箭的数量。
# 输入:  [[10,16], [2,8], [1,6], [7,12]]
# 输出:  2
# 说明:
# 一种方案是在坐标x=6射一支箭（可以刺破气球[2,8]和[1,6]），
# 在坐标x=11射另一只箭（刺破剩下的两个气球）
# 事实上，对于射在任何坐标x<f(1)上的箭能刺破的气球，射在f(1)上一定能刺破，
# 因为f(1)是所有右端点中最小的，在x上能刺破的气球右端点也不会小于f(1)。
# 这样我们就得到了一个贪心的策略：先按区间右端点f(i)排序，从左往右扫描区间，
# 取出当前右端点坐标最小的区间，在该区间右端点坐标x射出一箭，答案加1，
# 继续往后扫描，去掉所有能被这支箭刺破的气球（s(i)<=x的气球均能被刺破），
# 直到搜索到下一个不能被这只箭刺破的气球，再用同样的方式处理。时间复杂度为排序的时间复杂度O(n*log(n))。
def minimumnumberofarrowstoburstballoons(points):
    if points is None or len(points)==0:
        return 0
    points = sorted(points, key=lambda x:x[1])
    ans = 1
    lastEnd = points[0][1]
    for i in range(1,len(points)):
        # 右边的左区间比左边的右区间大，就多一次,并且lastend指向右边的右区间
        if points[i][0]>lastEnd:
            ans += 1
            lastEnd = points[i][1]
    return ans

print minimumnumberofarrowstoburstballoons([[1,6],[2,8],[7,12],[8,16]])