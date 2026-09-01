class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        output = []
        for s in strs:
            sort_s = ''.join(sorted(s))
            if sort_s in hash_map:
                hash_map[sort_s].append(s)
            else:
                hash_map[sort_s] = [s]

        for k in hash_map:
            output.append(hash_map[k])

        return output 

        