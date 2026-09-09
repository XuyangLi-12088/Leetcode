class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        max_heap = [-c for c in cnt.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = collections.deque()
        while max_heap or cooldown:
            time += 1

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

            if max_heap:
                remaining = heapq.heappop(max_heap) + 1
                if remaining:
                    cooldown.append((remaining, time + n + 1))
            
        return time
            

