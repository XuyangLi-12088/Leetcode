class Leaderboard:
    def __init__(self):
        self.hash_map = {} # key: player_id, value: score 

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.hash_map:
            self.hash_map[playerId] += score
        else:
            self.hash_map[playerId] = score
        return

    def top(self, K: int) -> int:
        max_heap = []
        for v in self.hash_map.values():
            max_heap.append(v * -1)
        heapq.heapify(max_heap)
        s = 0
        for _ in range(K):
            s += (heapq.heappop(max_heap) * -1)
        return s

    def reset(self, playerId: int) -> None:
        self.hash_map[playerId] = 0
        return

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)