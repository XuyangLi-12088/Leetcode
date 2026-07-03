class UnionFind:
    def __init__(self, n):  # 初始化
        self.fa = [i for i in range(n)]     # 每个元素的合集编号初始化为数组fa的下标索引

    def find(self, x):  # 查找元素根节点的合集编号内部实现方式
        while self.fa[x] != x:  # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.fa[self.fa[x]]    # 隔代压缩优化
            x = self.fa[x]
        return x    # 返回元素根节点的集合编号

    def union(self, x, y):  # 合并操作：令其中一个合集的树根节点指向另一个集合的树根节点
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:    # x和y的根节点集合编号相同，说明x和y已经同属于一个集合
            return False
        
        self.fa[root_x] = root_y    # x的根节点连接到y的根节点上，成为y的根节点的字节点
        return True

    def is_connected(self, x, y):   #查询操作：判断x和y是否同属于一个集合
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        # 遍历所有等式方程，将等式两边的单字母变量顶点进行合并。
        for equation in equations:
            if equation[1] == "=":
                index1 = ord(equation[0]) - 97
                index2 = ord(equation[3]) - 97
                union_find.union(index1, index2)

        # 遍历所有不等式方程，检查不等式两边的单字母遍历是不是在一个连通分量中，如果在则返回𝐹𝑎𝑙𝑠𝑒，否则继续扫描。如果所有不等式检查都没有矛盾，则返回 𝑇𝑟𝑢𝑒。
        for equation in equations:
            if equation[1] == "!":
                index1 = ord(equation[0]) - 97
                index2 = ord(equation[3]) - 97
                if union_find.is_connected(index1, index2):
                    return False
        return True
        