# coding=utf-8
# 如果对于每个直方块，找到从它开始往左边数第一个比它小的，和往右边数第一个比他小的，
# 则可以确定出以该直方块为最矮一块的矩阵的最大面积。使用数据结构栈，栈中保存递增序列，
# 从左到右依次遍历每个数让其入栈，入栈之前先pop出所有>=该数的数，从而保持栈中的递增序列。
# pop完之后的栈顶元素即为该数往左边数第一个比他小的数。同理反过来遍历一次可以得到往右边数第一个比他小的数。
# 时间复杂度O(n)，空间复杂度O(n)。
class Rectangle:
    def __init__(self):
        self.index = None
        self.height = 0
        self.left = 0
        self.right = 0
    def getMax(self,lists):
        stack = []
        if stack is None or len(stack)==0:
            return 0
        # 从左往右入栈
        for i in range(len(lists)):
            rectangle = lists.get(i)
            while len(stack)>0 and stack[-1].height >= lists.get(i).height:
                del(stack[-1])
            if len(stack)==0:
                rectangle.left = 0
            else:
                rectangle.left = stack[-1].index
            lists[i] = rectangle
            stack.append(rectangle)
        # 从右往左入栈
        for i in range(len(lists)-1,-1,-1):
            rectangle = lists[i]

            while len(stack)>0 and stack[-1].height >= lists.get(i).height:
                stack.pop()
            if len(stack)==0:
                rectangle.right = len(lists)+1
            else:
                rectangle.right = stack[-1].index
            lists[i] = rectangle
            stack.append(rectangle)
            max = (lists[0].right - lists[0].left-1)*lists[0].height
            print lists[0]

            for i in range(1,len(lists)):
                temp = (lists[i].right - lists[i].left-1)*lists[i].height
                print lists[i]
                if max<temp:
                    max = temp
            return max