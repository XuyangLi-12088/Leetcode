class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            if tuple(count) in hash_map:
                hash_map[tuple(count)].append(s)
            else:
                hash_map[tuple(count)] = [s]

        return list(hash_map.values())

        