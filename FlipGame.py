#coding=utf-8
# 你和你的朋友正在玩一个翻转游戏：给定一个只包含'+'和'-'的字符串，你和你的朋友轮流进行以下操作：
# 翻转两个连续的'+'，使得”++”变成”—”。无法进行操作的一方为输。那么给出一个字符串，
# 假设你先进行操作，你是否一定会赢呢？
# Example：
# s = "-++++-"
# 返回true，表示你一定会赢。只需翻转第二个和第三个加号使得
# s = "-+--+-"
# 此时对方无法继续操作（没有两个连续的加号）
class Solution:
    def canwin(self,s):
        state = [True]*len(s)
        for i in range(len(s)):
            if s[i] == '+':
                state[i] = True
            else:
                state[i] = False
        return self.search(state)

    def search(self,state):
        for i in range(len(state)-1):
            #如果是两个++，就反转成--
            if state[i] and state[i+1]:
                state[i] = False
                state[i+1] = False
                # 如果接下来全是false就胜利并反转回去供下一次反转，如果存在某种翻转使得子状态必败，那么该状态必胜
                if not self.search(state):
                    state[i] = True
                    state[i+1] = True
                    return True
                # 如果子状态还可以翻转就回溯
                else:
                    state[i] = True
                    state[i + 1] = True
        return False

    # def canWen2(self,s):
    #     nim = []*(len(s)+1)
    #     happen = []*(len(s)+1)
    #     for i in range(2,len(s)+1):
    #         for j in range(i-j-1):
    #             happen[nim[j]]^ nim[i-j-2]] =True
    #         nimEmpty = True
    #         for j in range(len(s)+1):
    #             if not happen[j] and nimEmpty:


s = Solution()
str = "++++++++"
print(s.canwin(str))
