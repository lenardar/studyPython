import sys
sys.path.append('.')
from module.Heap import MinBinaryHeap

# 实现优先级队列
# 基于堆实现
class PriorityQueue(MinBinaryHeap):
    def __init__(self):
        # 初始化一个二叉堆
        super().__init__()
    
    def enqueue(self, k):
        # 插入元素
        self.insert(k)
    
    def dequeue(self):
        # 删除最小元素
        return self.delMin()
    
    def isEmpty(self):
        # 判断队列是否为空
        return self.currentSize == 0
    
    def size(self):
        # 返回队列的大小
        return self.currentSize
    
    def peek(self):
        # 返回队列的最小元素
        return self.heapList[1]
    
    def buildHeap(self, alist):
        return super().buildHeap(alist)