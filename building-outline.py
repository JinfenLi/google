# coding=utf-8
class HashHeap:
    def __init__(self):
        self.heap = [0]
        self.hash = {}

    def add(self, key, value):
        self.heap.append((key, value))
        self.hash[key] = self.heap[0] + 1
        self.heap[0] += 1
        self._siftup(self.heap[0])

    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.heap[0])
        del self.hash[self.heap[self.heap[0]][0]]
        self.heap.pop()
        self.heap[0] -= 1
        if index <= self.heap[0]:
            index = self._siftup(index)
            self._siftdown(index)

    def hasKey(self, key):
        return key in self.hash

    def max(self):
        return 0 if self.heap[0] == 0 else self.heap[1][1]

    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hash[self.heap[a][0]] = a
        self.hash[self.heap[b][0]] = b

    def _siftup(self, index):
        while index != 1:
            if self.heap[index][1] <= self.heap[index / 2][1]:
                break
            self._swap(index, index / 2)
            index = index / 2
        return index

    def _siftdown(self, index):
        size = self.heap[0]
        while index < size:
            t = index
            if index * 2 <= size and self.heap[t][1] < self.heap[index * 2][1]:
                t = index * 2
            if index * 2 + 1 <= size and self.heap[t][1] < self.heap[index * 2 + 1][1]:
                t = index * 2 + 1
            if t == index:
                break
            self._swap(index, t)
            index = t
        return index


class Solution:
    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def buildingOutline(self, buildings):
        if len(buildings) == 0:
            return []

        begins = [(b[0], b[2], index) for index, b in enumerate(buildings)]
        ends = [(b[1], b[2], index) for index, b in enumerate(buildings)]
        heights = sorted(begins + ends, key=lambda x: x[0])
        print heights
        hashheap = HashHeap()
        y = {}
        # 当遇到同一个Index的时候即遇到右边的端点，将其删掉
        for x, height, index in heights:
            if hashheap.hasKey(index):
                hashheap.remove(index)
            else:
                hashheap.add(index, height)
            y[x] = hashheap.max()
        print y
        temp = []
        lastX, lastY = None, None
        for x in sorted(y.keys()):
            if lastX is not None and lastY != 0:
                temp.append((lastX, x, lastY))
            lastX, lastY = x, y[x]
        print temp,"temp"
        results = []
        lastInterval = temp[0]
        for start, end, height in temp[1:]:
            # 两座大厦重叠 Y[i] == Y[i-1]，此时在轮廓线上并无区别，那么 (Xi, Yi) 便不需要输出。
            if start == lastInterval[1] and height == lastInterval[2]:
                lastInterval = lastInterval[0], end, height
            else:
                results.append(lastInterval)
                lastInterval = (start, end, height)
        results.append(lastInterval)
        return results

s = Solution()
print s.buildingOutline([ [2 ,9 ,10], [3, 7, 15], [5 ,12, 12], [15, 20, 10], [19, 24, 8] ])