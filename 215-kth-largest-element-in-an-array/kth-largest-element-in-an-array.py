class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target_index = n - k
        left, right = 0, n - 1
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                return nums[i]
            if i > target_index:
                right = i - 1
            else:
                left = i + 1

    def partition(self, nums, left, right):
        i = randint(left, right)
        pivot = nums[i]
        nums[i], nums[left] = nums[left], nums[i]

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1

            while i <= j and nums[j] > pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums[left], nums[j] = nums[j], nums[left]

        return j

    # def findKthLargest(self, nums: List[int], k: int) -> int:

    #     # Using Heap
    #     negative_nums = []

    #     for i in range(len(nums)):
    #         negative_nums.append(nums[i] * -1)

    #     heapq.heapify(negative_nums)

    #     while k != 1:
    #         heapq.heappop(negative_nums)
    #         k -= 1

    #     return heapq.heappop(negative_nums) * -1

