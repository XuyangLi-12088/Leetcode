class Leaderboard:
    # (score, player_id)
    def __init__(self):
        self.hash_map = {} # key: player_id, value: score 

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.hash_map:
            self.hash_map[playerId] += score
        else:
            self.hash_map[playerId] = score
        return

    def top(self, K: int) -> int:
        score_list = list(self.hash_map.values())
        score_list.sort(reverse=True)
        return sum(score_list[0:K])

    def reset(self, playerId: int) -> None:
        self.hash_map[playerId] = 0
        return

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)