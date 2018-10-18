#coding=utf-8
# 一个长条花坛里有若干并排的花槽，有些花槽中已经种了花，有些则还没种花。
# 然而，不能将两株花种在相邻的花槽否则它们会争夺水分导致两者都枯萎。
# 给定一个花坛的种植情况flowerbed（一个包含0和1的数组，0表示该花槽为空，1表示该花槽已经种了花），
# 以及一个数n，问是否可以再种下新的n株花且满足相邻花槽不能同时种花的条件。
def canPlaceFlower(flowerbed,n):
    count = 0
    #连续3个零则在中间种花
    for i in range(len(flowerbed)):
        if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1]==0) and
                (i == len(flowerbed)-1 or flowerbed[i+1]==0)):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
    return False