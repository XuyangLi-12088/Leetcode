class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_r = collections.Counter(ransomNote)
        counter_m = collections.Counter(magazine)
        for key in counter_r:
            if counter_r[key] > counter_m[key]:
                return False
        return True 