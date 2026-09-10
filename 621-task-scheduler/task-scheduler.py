class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        max_heap = [(-cnt[k], k) for k in cnt]
        heapq.heapify(max_heap)

        time = 0
        cooldown = collections.deque()
        output = []
        while max_heap or cooldown:
            time += 1

            if cooldown and cooldown[0][2] == time:
                r, k, _ = cooldown.popleft()
                heapq.heappush(max_heap, (r, k))

            if max_heap:
                c, k = heapq.heappop(max_heap)
                remaining = c + 1
                if remaining != 0:
                    output.append(k)
                    cooldown.append((remaining, k, time + n + 1))
            
        return time