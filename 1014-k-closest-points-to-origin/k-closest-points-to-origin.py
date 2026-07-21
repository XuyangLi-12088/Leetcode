class Solution:
    def euc_distance(self, x: List[int], y: List[int]) -> int:
        return ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        heap = []
        for i in range(len(points)):
            cur_distance = -self.euc_distance([points[i][0], 0], [points[i][1], 0])
            # heap未满，直接加进heap
            if len(heap) < k:
                heapq.heappush(heap, (cur_distance, i))
            # heap满了
            else:
                max_distance = heap[0][0]
                if cur_distance > max_distance:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cur_distance, i))

        for p in heap:
            output.append(points[p[1]])

        return output

        