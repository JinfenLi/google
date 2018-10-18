#coding=utf-8

import numpy as np
class Subset:
    def getSubsets(self, A, n):
        result = [[A[0]]]
        for i in range(1, n):
            tmp = result[:]
            for j in range(len(tmp)):
                if [A[i]] + tmp[j] not in result:
                    tmp[j] = [A[i]] + tmp[j]
            # 加上他单独自己
            if [A[i]] not in result:
                result = tmp + [[A[i]]] + result
            else:
                result = tmp + result
        # result = self.removedup(result)
        return result

    def getSubsets2(self,A,n):
        A = np.array(A)
        a=[]

        for i in range(2**n):
            e = list(bin(i))[2:]
            e = np.array(e) == '1'
            a.append((A[n-len(e):][e]).tolist())
        a = self.removedup(a)
        print a

    def removedup(self,A):
        b = []
        for i in range(len(A)):
            if A[i] not in b:
                b.append(A[i])
        # print a
        A = b
        return A

s = Subset()
# print s.getSubsets([1,2,2],3)
print s.getSubsets(['A','B','B'],3)