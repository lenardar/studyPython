# 实现图算法
# 使用两个类，Graph类存储包含所有带点的主列表，Vertex类存储每个顶点的信息

# 实现Vertex类
class Vertex():
    def __init__(self, key):
        # 顶点的id
        self.id = key
        # 顶点的连接,以字典的形式存储，key是顶点对象，value是权重
        self.connectedTo = {}
    
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
        return iter(self.vertList.values())


# 实现广度优先搜索
def bfs(gragh, start):
    start.setDistance(0)  # 起始点的距离为0
    start.setPred(None)  # 起始点的前驱为None
    vertQueue = Queve()  # 创建一个队列
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
    vertQueue = Queve()  # 创建一个队列
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