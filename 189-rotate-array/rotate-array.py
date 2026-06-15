class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # while (k != 0):
        #     last_element = nums.pop(-1)
        #     nums.insert(0, last_element)
        #     k -= 1 

        k %= len(nums)
        last_k = nums[len(nums)-k:]
        rest = nums[:len(nums)-k]
        nums[:] = last_k + rest



        