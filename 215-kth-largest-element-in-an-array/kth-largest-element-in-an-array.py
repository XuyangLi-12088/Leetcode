class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Using Heap
        negative_nums = []

        for i in range(len(nums)):
            negative_nums.append(nums[i] * -1)

        heapq.heapify(negative_nums)

        while k != 1:
            heapq.heappop(negative_nums)
            k -= 1

        return heapq.heappop(negative_nums) * -1

