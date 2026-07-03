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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = set()
        num_city = len(isConnected)
        union_find = UnionFind(num_city)
        for i in range(num_city):
            for j in range(i+1, num_city):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        
        for city in range(num_city):
            res.add(union_find.find(city))

        return len(res)



        