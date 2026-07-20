class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # hash table solution
        # hash_table = {}

        # for n in nums:
        #     if (n in hash_table):
        #         hash_table[n] += 1
        #         if (hash_table[n] >= 2):
        #             return True
        #     else:
        #         hash_table[n] = 1

        # return False


        # set solution
        s = set()

        for n in nums:
            s.add(n)

        if (len(s) != len(nums)):
            return True
        else:
            return False
