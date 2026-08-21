class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hash_map = {}
        for i, c in enumerate(s):
            if c not in hash_map:
                hash_map[c] = [i, i]
            else:
                hash_map[c][1] = i

        start = hash_map[s[0]][0]
        end = hash_map[s[0]][1]
        for key in hash_map:
            s, e = hash_map[key]
            if s > end:
                res.append(end - start + 1)
                start = s
                end = e
            else:
                if e > end:
                    end = e

        res.append(end - start + 1)

        return res