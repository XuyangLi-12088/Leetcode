class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        # start Topological sorting
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1

        queue = collections.deque()
        for u in indegrees:
            if indegrees[u] == 0:
                queue.append(u)
        order = []

        while queue:
            pop = queue.popleft()
            order.append(pop)
            for v in graph[pop]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
            
        if len(order) != len(indegrees):
            return False
        
        return True
        