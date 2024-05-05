# 实现图算法
# 使用两个类，Graph类存储包含所有带点的主列表，Vertex类存储每个顶点的信息
# 将module文件夹添加到sys.path中，以便导入module模块
import sys
sys.path.append('.')
from module.Queue import Queue
from module.Stack import Stack

# 实现Vertex类
class Vertex():
    def __init__(self, key):
        # 顶点的id
        self.id = key
        # 顶点的连接,以字典的形式存储，key是顶点对象，value是权重
        self.connectedTo = {}
        
        # 针对广度优先搜索的辅助变量
        self.color = 'white'  # 顶点的颜色，白色表示未访问，灰色表示访问过但未探索，黑色表示访问过且探索过
        self.dist = 0  # 顶点的距离
        self.pred = None  # 顶点的前驱
        
        # 针对深度优先搜索的辅助变量
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self, nbr, weight=0):
        # 添加邻接顶点
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        # 返回顶点的连接信息
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        # 返回所有连接的顶点
        return self.connectedTo.keys()
    
    def getId(self):
        # 返回顶点的id
        return self.id
    
    def getWeight(self, nbr):
        # 返回顶点的权重
        return self.connectedTo[nbr]
    
    # 针对广度优先搜索的辅助函数
    # 针对广度优先搜索的辅助函数
    # 针对广度优先搜索的辅助函数
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setDistance(self, d):
        self.dist = d
        
    def getDistance(self):
        return self.dist
    
    def setPred(self, p):
        self.pred = p
        
    def getPred(self):
        return self.pred
    
    # 针对深度优先搜索的辅助函数
    # 针对深度优先搜索的辅助函数
    # 针对深度优先搜索的辅助函数
    def setDiscovery(self, dtime):
        self.disc = dtime
        
    def getDiscovery(self):
        return self.disc
    
    def setFinish(self, ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin


# 实现Graph类
class Graph():
    def __init__(self):
        # 图的顶点列表
        self.vertList = {}
        # 顶点的个数
        self.numVertices = 0
    
    def addVertex(self, key):
        # 添加顶点
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        # 返回顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def __contains__(self, n):
        # 判断顶点是否在图中
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        # 添加边
        # f是起点，t是终点，cost是权重
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    def getVertices(self):
        # 返回所有顶点
        return self.vertList.keys()
    
    def __iter__(self):
        # 迭代器
        # 返回所有顶点
        # 形式为每一个顶点相连的所以顶点
        return iter(self.vertList.values())


# 实现广度优先搜索
def bfs(gragh, start):
    start.setDistance(0)  # 起始点的距离为0
    start.setPred(None)  # 起始点的前驱为None
    vertQueue = Queue()  # 创建一个队列
    vertQueue.enqueue(start)  # 起始点入队
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()  # 出队
        for nbr in currentVert.getConnections():
            # 遍历当前顶点的所有邻接顶点
            nbr.setColor('gray')  # 邻接顶点变为灰色,表示已经访问过
            nbr.setDistance(currentVert.getDistance() + 1)  # 邻接顶点的距离为当前顶点的距离加1
            nbr.setPred(currentVert)  # 邻接顶点的前驱为当前顶点
            vertQueue.enqueue(nbr)  # 邻接顶点入队
        currentVert.setColor('black')  # 当前顶点变为黑色，表示已经探索过


# 回溯，找到从起始点到终点的路径
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


# 优化广义优先搜索算法，不必遍历所有的顶点，只需要遍历到终点即可
# 返回路径
def bfsAdjust(gragh, start, end):
    # start是起始点，end是终点
    start.setDistance(0)  # 起始点的距离为0
    start.setPred(None)  # 起始点的前驱为None
    vertQueue = Queue()  # 创建一个队列
    # 起始点入队
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()  # 出队
        if currentVert == end:
            # 如果当前顶点是终点，返回路径
            traverse(currentVert)
            return
        for nbr in currentVert.getConnections():
            # 遍历当前顶点的所有邻接顶点
            if nbr.getColor() == 'white':
                # 如果邻接顶点未访问过
                nbr.setColor('gray')  # 邻接顶点变为灰色,表示已经访问过
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
    return None

# 实现深度有限搜索
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def dfs(self):
        # 深度优先搜索
        for aVertex in self:
            # 初始化所有顶点
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                # 如果顶点未访问过
                self.dfsvisit(aVertex)
        
    def dfsvisit(self, startVertex):
        # 深度优先搜索的辅助函数
        startVertex.setColor('gray')  # 顶点变为灰色，表示已经访问过
        self.time += 1  # 时间加1
        startVertex.setDiscovery(self.time)  # 设置发现时间
        for nextVertex in startVertex.getConnections():
            # 遍历所有邻接顶点
            if nextVertex.getColor() == 'white':
                # 如果邻接顶点未访问过
                nextVertex.setPred(startVertex)  # 设置邻接顶点的前驱
                self.dfsvisit(nextVertex)  # 递归调用
        startVertex.setColor('black')  # 顶点变为黑色，表示已经探索过
        self.time += 1  # 时间加1
        startVertex.setFinish(self.time)  # 设置完成时间
    
    def dfsAdjust(self, start, end):
        # 深度优先搜索，找到从起始点到终点的路径
        start.setColor('white')
        start.setPred(None)
        stack = Stack()
        stack.push(start)
        while not stack.isEmpty():
            currentVertex = stack.pop()
            if currentVertex == end:
                traverse(currentVertex)
                return
            for nbr in currentVertex.getConnections():
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                    nbr.setPred(currentVertex)
                    stack.push(nbr)
            currentVertex.setColor('black')
        return None