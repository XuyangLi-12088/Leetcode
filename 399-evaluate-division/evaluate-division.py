class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.multiples = [1 for _ in range(n)]

    def find(self, x):
        multiple = 1.0
        origin = x
        while x != self.parent[x]:
            multiple *= self.multiples[x]
            x = self.parent[x]
        self.parent[origin] = x
        self.multiples[origin] = multiple
        return x

    def union(self, x, y, multiple):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.multiples[root_x] = multiple * self.multiples[y] / self.multiples[x]
        return

    def is_connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            return -1.0
        return self.multiples[x] / self.multiples[y]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equations_size = len(equations)
        hash_map = {}
        union_find = UnionFind(2 * equations_size)

        id = 0
        for i in range(equations_size):
            equation = equations[i]
            var1, var2 = equation[0], equation[1]
            if var1 not in hash_map:
                hash_map[var1] = id
                id += 1
            if var2 not in hash_map:
                hash_map[var2] = id
                id += 1
            union_find.union(hash_map[var1], hash_map[var2], values[i])

        queries_size = len(queries)
        res = []
        for i in range(queries_size):
            query = queries[i]
            var1, var2 = query[0], query[1]
            if var1 not in hash_map or var2 not in hash_map:
                res.append(-1.0)
            else:
                id1 = hash_map[var1]
                id2 = hash_map[var2]
                res.append(union_find.is_connected(id1, id2))

        return res
        