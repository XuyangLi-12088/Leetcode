# 拓扑排序 (Topological Sorting)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建图
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        # 开始拓扑排序
        indegrees = {u: 0 for u in graph}   # indegrees用于记录所有顶点的入度
        # 统计所有顶点的入度
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1

        # 将入度为0的顶点存入集合S中
        S = collections.deque([u for u in indegrees if indegrees[u] == 0])
        order = []  # order用于存储拓扑排序

        while S:
            u = S.pop()     # 从集合中选择一个入度为0的顶点
            order.append(u)     # 将其输出到拓扑排序order中
            # 遍历顶点u的所有邻接节点v
            for v in graph[u]:
                indegrees[v] -= 1   # 删除从顶点u出发的有向边
                if indegrees[v] == 0:   # 如果删除该边后顶点v的入度变为0
                    S.append(v)     # 将其放入集合S中
        
        if len(indegrees) != len(order): # 还有顶点未遍历（存在环），无法构成拓扑排序
            return []
        return order



        