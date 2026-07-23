# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # BFS Solution:
#         res = 0
#         if not grid[0]:
#             return 0
        
#         queue = deque()

#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == "1":
#                     res += 1
#                     queue.append((i, j))
#                     grid[i][j] = "0"
#                     while len(queue) != 0:
#                         pop = queue.popleft()
#                         if (pop[0]-1) >= 0 and grid[pop[0]-1][pop[1]] == "1":
#                             queue.append((pop[0]-1, pop[1]))
#                             grid[pop[0]-1][pop[1]] = "0"
#                         if (pop[0]+1) < len(grid) and grid[pop[0]+1][pop[1]] == "1":
#                             queue.append((pop[0]+1, pop[1]))
#                             grid[pop[0]+1][pop[1]] = "0"
#                         if (pop[1]-1) >= 0 and grid[pop[0]][pop[1]-1] == "1":
#                             queue.append((pop[0], pop[1]-1))
#                             grid[pop[0]][pop[1]-1] = "0"
#                         if (pop[1]+1) < len(grid[0]) and grid[pop[0]][pop[1]+1] == "1":
#                             queue.append((pop[0], pop[1]+1))
#                             grid[pop[0]][pop[1]+1] = "0"

#         return res


    #     # DFS Solution:
    #     res = 0
        
    #     if not grid[0]:
    #         return 0
        
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == "1":
    #                 res += 1
    #                 self.dfs(grid, i, j)

    #     return res

    # def dfs(self, grid, i, j):
    #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
    #         return
        
    #     if grid[i][j] == "0":
    #         return

    #     if grid[i][j] == "1":
    #         grid[i][j] = "0"

    #     self.dfs(grid, i-1, j)
    #     self.dfs(grid, i+1, j)
    #     self.dfs(grid, i, j-1)
    #     self.dfs(grid, i, j+1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        output = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    queue = collections.deque()
                    visited = set()
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        pop = queue.popleft()
                        grid[pop[0]][pop[1]] = '0'
                        # up
                        if (pop[0] - 1, pop[1]) not in visited and 0 <= pop[0] - 1 < h and grid[pop[0] - 1][pop[1]] == "1":
                            queue.append((pop[0] - 1, pop[1]))
                            visited.add((pop[0] - 1, pop[1]))
                        # down
                        if (pop[0] + 1, pop[1]) not in visited and 0 <= pop[0] + 1 < h and grid[pop[0] + 1][pop[1]] == "1":
                            queue.append((pop[0] + 1, pop[1]))
                            visited.add((pop[0] + 1, pop[1]))
                        # left
                        if (pop[0], pop[1] - 1) not in visited and 0 <= pop[1] - 1 < w and grid[pop[0]][pop[1] - 1] == "1":
                            queue.append((pop[0], pop[1] - 1))
                            visited.add((pop[0], pop[1] - 1))
                        # right
                        if (pop[0], pop[1] + 1) not in visited and 0 <= pop[1] + 1 < w and grid[pop[0]][pop[1] + 1] == "1":
                            queue.append((pop[0], pop[1] + 1))
                            visited.add((pop[0], pop[1] + 1))

                    output += 1

        return output
        

