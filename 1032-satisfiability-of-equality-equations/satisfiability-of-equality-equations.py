class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        
        self.fa[root_x] = root_y
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        for equation in equations:
            if equation[1] == "=":
                index1 = ord(equation[0]) - 97
                index2 = ord(equation[3]) - 97
                union_find.union(index1, index2)

        for equation in equations:
            if equation[1] == "!":
                index1 = ord(equation[0]) - 97
                index2 = ord(equation[3]) - 97
                if union_find.is_connected(index1, index2):
                    return False
        return True
        