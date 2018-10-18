#coding = utf-8
# 给出包含n个整数的数组，你的任务是检查它是否可以通过修改至多一个元素变成非下降的。
# 一个非下降的数组array对于所有的i（1<=i<n）满足array[i-1]<=array[i]。n属于区间[1,10000]。
# 整个数组有零组或一组下降相邻数组，若只有一组还要判断改的前后是否能连接成非下降数组
def checkPossibility(nums):
    pos =0
    count = 0
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            pos = i
            count += 1
    if count ==0:
        return True
    if count>1:
        return False
    return pos == 1 or pos == len(nums)-1 or nums[pos-2]<=nums[pos]

print checkPossibility([2,4,3,3])