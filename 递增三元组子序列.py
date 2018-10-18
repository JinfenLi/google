# coding=utf-8
import sys
def increasingTriplet(nums):
    first = sys.maxint
    second = sys.maxint
    for n in nums:
        #  一直没有递增序列则指向最后一个数
        if n <= first:
            first = n
            continue
        # second记录
        if first<n and n<= second:
            second = n
            continue
        if n>second:
            return True
    return False
print increasingTriplet([3,3,1,6,7])