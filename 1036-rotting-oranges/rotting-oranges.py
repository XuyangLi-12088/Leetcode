class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        output = 0
        queue = collections.deque()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            queue_size = len(queue)
            flag = False
            for _ in range(queue_size):
                pop = queue.popleft()
                # up
                if 0 <= pop[0] - 1 < h and grid[pop[0] - 1][pop[1]] == 1:
                    grid[pop[0] - 1][pop[1]] = 2
                    queue.append((pop[0] - 1, pop[1]))
                    flag = True
                # down
                if 0 <= pop[0] + 1 < h and grid[pop[0] + 1][pop[1]] == 1:
                    grid[pop[0] + 1][pop[1]] = 2
                    queue.append((pop[0] + 1, pop[1]))
                    flag = True
                # left
                if 0 <= pop[1] - 1 < w and grid[pop[0]][pop[1] - 1] == 1:
                    grid[pop[0]][pop[1] - 1] = 2
                    queue.append((pop[0], pop[1] - 1))
                    flag = True
                # right
                if 0 <= pop[1] + 1 < w and grid[pop[0]][pop[1] + 1] == 1:
                    grid[pop[0]][pop[1] + 1] = 2
                    queue.append((pop[0], pop[1] + 1))
                    flag = True

            if flag == True:
                output += 1

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    return -1

        return output