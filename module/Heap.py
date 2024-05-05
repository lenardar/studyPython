# 构建二叉堆
class MinBinaryHeap():
    def __init__(self):
        self.heapList = [0]  # 二叉堆的存储列表
        self.currentSize = 0  # 二叉堆的大小

    def percUp(self, i):
        # 从i开始向上调整,使得二叉堆满足堆的性质,即父节点的值小于子节点的值
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, k):
        # 插入元素,并调整二叉堆
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        # 从i开始向下调整,使得二叉堆满足堆的性质,即父节点的值小于子节点的值
        while i * 2 <= self.currentSize:
            mc = self.MinChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def MinChild(self, i):
        # 找到i节点的最小子节点
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # 删除最小元素,并调整二叉堆
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        # 从alist中构建二叉堆
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1


# 实现最大堆
class MaxBinaryHeap():
    def __init__(self):
        self.heaplist = [0]  # 二叉堆的存储列表
        self.currentSize = 0  # 二叉堆的大小

    def percUp(self, i):
        # 从i开始向上调整,使得二叉堆满足堆的性质,即父节点的值大于子节点的值
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i//2]:  # 这里与最小堆区别
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, k):
        # 插入元素,并调整二叉堆
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        # 从i开始向下调整,使得二叉堆满足堆的性质,即父节点的值大于子节点的值
        while i * 2 <= self.currentSize:
            mc = self.getMaxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def getMaxChild(self, i):
        # 找到i节点的最大子节点
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i*2] > self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        # 删除最大元素,并调整二叉堆
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        # 从alist中构建二叉堆
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
