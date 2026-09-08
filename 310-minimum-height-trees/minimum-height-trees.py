class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        indegrees = {}
        graph = {}
        for e in edges:
            if e[0] in indegrees:
                indegrees[e[0]] += 1
            else:
                indegrees[e[0]] = 1
            if e[1] in indegrees:
                indegrees[e[1]] += 1
            else:
                indegrees[e[1]] = 1

            if e[0] in graph:
                graph[e[0]].append(e[1])
            else:
                graph[e[0]] = [e[1]]
            if e[1] in graph:
                graph[e[1]].append(e[0])
            else:
                graph[e[1]] = [e[0]]

        queue = collections.deque([v for v in indegrees if indegrees[v] == 1])
        ans = []
        while queue:
            ans = []
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append(node)
                for n in graph[node]:
                    indegrees[n] -= 1
                    if indegrees[n] == 1:
                        queue.append(n)
        
        return ans