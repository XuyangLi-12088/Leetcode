class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        # start Topological sorting
        indegrees = {v: 0 for v in graph}
        for v in graph:
            for n in graph[v]:
                indegrees[n] += 1

        order = []
        S = collections.deque([v for v in indegrees if indegrees[v] == 0])

        while S:
            v = S.popleft()
            order.append(v)
            for n in graph[v]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    S.append(n)

        if len(order) != len(graph):
            return False

        return True
        