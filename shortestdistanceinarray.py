#coding=utf-8
import sys
class Solution:
    def shortestDistance(self,grid):
        row = len(grid)
        column = len(grid[0])
        if row == 0 or column == 0 or not self.haveZeros(grid,row,column):
            return -1
        rowSum = [0] * row
        columnSum = [0] * column
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    rowSum[i] += 1
                    columnSum[j] += 1
        ansRow = [None] * row
        ansColumn = [None] * column
        self.getSumDistance(rowSum,row,ansRow)
        self.getSumDistance(columnSum,column,ansColumn)

        ans = sys.maxint
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and ans>ansRow[i]+ansColumn[j]:
                    ans = ansRow[i]+ansColumn[j]
        return ans


    def getSumDistance(self,aSum,n,ans):
        prefixSum1 = [0] * n
        prefixSum2 = [0] * n
        # 处理前缀
        prefixSum1[0] = aSum[0]
        for i in range(1,n):
            prefixSum1[i] = prefixSum1[i-1]+aSum[i]
        prefixSum2[0] = 0
        for j in range(1,n):
            prefixSum2[j] = prefixSum2[j-1] + prefixSum1[j-1]
        for i in range(n):
            ans[i] = prefixSum2[i]
        #处理后缀
        prefixSum1[n-1] = aSum[n-1]
        for i in range(n-2,-1,-1):
            prefixSum1[i] = prefixSum1[i+1]+aSum[i]
        prefixSum2[n - 1] = 0
        for i in range(n-2,-1,-1):
            prefixSum2[i] = prefixSum1[i+1]+prefixSum2[i+1]
        for i in range(n):
            ans[i] += prefixSum2[i]




    def haveZeros(self,grid, row, column):
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    return True
        return False