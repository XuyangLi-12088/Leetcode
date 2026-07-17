class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = collections.Counter(s)
        for c in t:
            if c in hash_map and hash_map[c] != 0:
                hash_map[c] -= 1
            else:
                return False

        for key in hash_map:
            if hash_map[key] != 0:
                return False

        return True


