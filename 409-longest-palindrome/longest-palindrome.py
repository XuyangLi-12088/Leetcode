class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        hash_map = collections.Counter(s)
        for l in hash_map:
            # 如果是偶数
            if hash_map[l] % 2 == 0:
                output += hash_map[l]
                hash_map[l] -= hash_map[l]
            # 如果是奇数
            else:
                output += hash_map[l] - hash_map[l] % 2
                hash_map[l] -= hash_map[l] - hash_map[l] % 2
            
        for l in hash_map:
            if hash_map[l] != 0:
                return output + 1

        return output

