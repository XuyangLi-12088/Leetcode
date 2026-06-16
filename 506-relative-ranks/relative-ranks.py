class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0] * len(score)
        hash_map = {}
        for i, s in enumerate(score):
            hash_map[s] = i

        score.sort()
        place = 1
        for i in range(len(score) - 1, -1, -1):
            if place == 1:
                ans[hash_map[score[i]]] = "Gold Medal"
            elif place == 2:
                ans[hash_map[score[i]]] = "Silver Medal"
            elif place == 3:
                ans[hash_map[score[i]]] = "Bronze Medal"
            else:
                ans[hash_map[score[i]]] = str(place)
            place += 1

        return ans
        
