class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_cnt = Counter(arr1)
        output = []
        nums_not_in_arr2 = []
        for n in arr1:
            if n not in set(arr2):
                nums_not_in_arr2.append(n)
        nums_not_in_arr2.sort()

        for n in arr2:
            for _ in range(arr1_cnt[n]):
                output.append(n)

        return output + nums_not_in_arr2
        