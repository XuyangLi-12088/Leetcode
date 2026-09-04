class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        output = []
        changed_cnt = Counter(changed)
        changed.sort()
        # [1, 2, 3, 4, 6, 8]
        for n in changed:
            if changed_cnt[n] == 0:
                continue
            if n*2 in changed_cnt and changed_cnt[n*2] != 0:
                output.append(n)
                changed_cnt[n] -= 1
                changed_cnt[n*2] -= 1
            else:
                return []
            
        return output


        