class Solution:
    def euc_distance(self, x: List[int], y: List[int]) -> int:
        return ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        heap = []
        for i in range(len(points)):
            heap.append((self.euc_distance([points[i][0], 0], [points[i][1], 0]), i))

        heapq.heapify(heap)

        for _ in range(k):
            output.append(points[heapq.heappop(heap)[1]])

        return output

        