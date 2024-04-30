# 实现二叉搜索树

# 定义BinarySearchTree类
class BinarySearchTree():
    def __init__(self):
        self.root = None  # 二叉搜索树的根节点
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        # 插入键值对,如果没有根节点,则将插入的键值对作为根节点,否则调用_put函数
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        # 插入键值对,如果当前节点的键值大于插入的键值,则将插入的键值对插入到左子树,否则插入到右子树
        if key < currentNode.key:
            # 小于当前节点的键值，插入左子树
            if currentNode.hasLeftChild():
                # 如果有左子树，调用函数
                self._put(key, val, currentNode.leftChild)
            else:
                # 如果没有左子树，则插入
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        elif key > currentNode.key:
            # 大于当前节点的键值，插入右子树
            if currentNode.hasRightChild():
                # 如果有右子树，调用函数
                self._put(key, val, currentNode.rightChild)
            else:
                # 如果没有右子树，则插入
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        else:
            # 重复键值处理，更新值
            currentNode.value = val

    def __setitem__(self, k, v):
        # 重载[]操作符
        self.put(k, v)

    def get(self, key):
        # 获取键值对
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        # 获取键值对
        if not currentNode:
            return None
        if key == currentNode.key:
            return currentNode
        if key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        # 重载[]操作符
        return self.get(key)

    def __contains__(self, key):
        # 判断键值对是否存在
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        # 删除键值对
        if self.size > 1:
            currentNode = self._get(key, self.root)
            if currentNode:
                self.remove(currentNode)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        # 重载[]操作符
        self.delete(key)

    def remove(self, currentNode):
        # 删除节点
        if currentNode.isLeaf():
            # 叶节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            # 有两个子节点
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.value = succ.value
        else:
            # 只有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.value,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.value,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

    def findSuccessor(self):
        # 找到后继节点
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        # 找到最小节点
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        # 删除节点
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


# 定义TreeNode类
class TreeNode():
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key  # 键
        self.value = val  # 节点的值
        self.leftChild = left  # 左子树
        self.rightChild = right  # 右子树
        self.parent = parent

    def hasLeftChild(self):
        # 判断是否有左子树
        return self.leftChild

    def hasRightChild(self):
        # 判断是否有右子树
        return self.rightChild

    def isLeftChild(self):
        # 判断是否为左子树,如果父节点不为空,且当前节点为父节点的左子树,则返回True
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        # 判断是否为右子树,如果父节点不为空,且当前节点为父节点的右子树,则返回True
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        # 判断是否为根节点
        return not self.parent

    def isLeaf(self):
        # 判断是否为叶节点
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        # 判断是否有子节点
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        # 判断是否有两个子节点
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        # 替换节点数据
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
