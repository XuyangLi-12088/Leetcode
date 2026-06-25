# # 优先队列解法:
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         size = len(nums)
#         q = [(-nums[i], i) for i in range(k)]
#         heapq.heapify(q)
#         res = [-q[0][0]]
#         for i in range(k, size):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= i - k:
#                 heapq.heappop(q)
#             res.append(-q[0][0])
#         return res

# Solution 1:
# class MyQueue:
#     def __init__(self):
#         self.queue = deque()

#     def pop(self, value):
#         if self.queue and value == self.queue[0]:
#             self.queue.popleft()

#     def push(self, value):
#         while self.queue and value > self.queue[-1]:
#             self.queue.pop()
#         self.queue.append(value)

#     def front(self):
#         return self.queue[0]

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         que = MyQueue()
#         result = []
#         for i in range(k):
#             que.push(nums[i])
#         result.append(que.front())
#         for i in range(k, len(nums)):
#             que.pop(nums[i - k])
#             que.push(nums[i])
#             result.append(que.front())
#         return result

# Solution 2:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        kept_nums = deque()

        for i in range(len(nums)):
            self.update_kept_nums(kept_nums, nums[i])

            if i >= k and nums[i - k] == kept_nums[0]:
                kept_nums.popleft()

            if i >= k - 1:
                max_list.append(kept_nums[0])

        return max_list

    def update_kept_nums(self, kept_nums, num):
        while kept_nums and num > kept_nums[-1]:
            kept_nums.pop()

        kept_nums.append(num)