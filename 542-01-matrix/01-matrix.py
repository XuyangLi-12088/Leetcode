class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        output = [[0 for _ in range(w)] for _ in range(h)]
        queue = collections.deque()
        visited = set()
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                pop = queue.popleft()
                pop_distance = output[pop[0]][pop[1]]
                # up
                if 0 <= pop[0] - 1 < h and (pop[0] - 1, pop[1]) not in visited:
                    queue.append((pop[0] - 1, pop[1]))
                    visited.add((pop[0] - 1, pop[1]))
                    output[pop[0] - 1][pop[1]] = pop_distance + 1
                # down
                if 0 <= pop[0] + 1 < h and (pop[0] + 1, pop[1]) not in visited:
                    queue.append((pop[0] + 1, pop[1]))
                    visited.add((pop[0] + 1, pop[1]))
                    output[pop[0] + 1][pop[1]] = pop_distance + 1
                # left
                if 0 <= pop[1] - 1 < w and (pop[0], pop[1] - 1) not in visited:
                    queue.append((pop[0], pop[1] - 1))
                    visited.add((pop[0], pop[1] - 1))
                    output[pop[0]][pop[1] - 1] = pop_distance + 1
                # right
                if 0 <= pop[1] + 1 < w and (pop[0], pop[1] + 1) not in visited: 
                    queue.append((pop[0], pop[1] + 1))
                    visited.add((pop[0], pop[1] + 1))
                    output[pop[0]][pop[1] + 1] = pop_distance + 1            
        
        return output
        
