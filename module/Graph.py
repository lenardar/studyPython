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