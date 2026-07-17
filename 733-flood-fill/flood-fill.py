class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        weight = len(image[0])
        queue = collections.deque()
        visited = set()
        queue.append((sr, sc))
        visited.add((sr, sc))
        start_color = image[sr][sc]
        while queue:
            curr = queue.popleft()
            # up
            if 0 <= curr[0] - 1 < height and (curr[0] - 1, curr[1]) not in visited and image[curr[0] - 1][curr[1]] == start_color:
                queue.append((curr[0] - 1, curr[1]))
                visited.add((curr[0] - 1, curr[1]))
            # down
            if 0 <= curr[0] + 1 < height and (curr[0] + 1, curr[1]) not in visited and image[curr[0] + 1][curr[1]] == start_color:
                queue.append((curr[0] + 1, curr[1]))
                visited.add((curr[0] + 1, curr[1]))
            # left
            if 0 <= curr[1] - 1 < weight and (curr[0], curr[1] - 1) not in visited and image[curr[0]][curr[1] - 1] == start_color:
                queue.append((curr[0], curr[1] - 1))
                visited.add((curr[0], curr[1] - 1))
            # right
            if 0 <= curr[1] + 1 < weight and (curr[0], curr[1] + 1) not in visited and image[curr[0]][curr[1] + 1] == start_color:
                queue.append((curr[0], curr[1] + 1))
                visited.add((curr[0], curr[1] + 1))

        for node in visited:
            print(node)
            image[node[0]][node[1]] = color

        return image