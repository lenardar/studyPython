# 队列
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # 入队
        self.items.insert(0, item)

    def dequeue(self):  # 出队
        return self.items.pop()

    def size(self):
        return len(self.items)
    


# 实现优先级队列
class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item, priority):  # 入队
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1], reverse=True)

    def dequeue(self):  # 出队
        return self.items.pop()

    def size(self):
        return len(self.items)