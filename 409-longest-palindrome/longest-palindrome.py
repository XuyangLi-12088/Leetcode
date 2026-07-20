class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        hash_map = collections.Counter(s)
        for l in hash_map:
            output += (hash_map[l] // 2) * 2
            hash_map[l] -= (hash_map[l] // 2) * 2
            
        for l in hash_map:
            if hash_map[l] != 0:
                return output + 1

        return output

