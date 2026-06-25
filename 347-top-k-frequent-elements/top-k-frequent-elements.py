class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash Map + Max Heap Solution:
        result = []
        hash_map = {}
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
            
        max_heap = []
        for key in hash_map:
            max_heap.append((-hash_map[key], key))
        heapq.heapify(max_heap)

        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result


        # # Hash Map + Min Heap Solution:
        # result = []
        # hash_map = {}
        # for n in nums:
        #     if n in hash_map:
        #         hash_map[n] += 1
        #     else:
        #         hash_map[n] = 1
            
        # min_heap = []
        # heapq.heapify(min_heap)
        # for key in hash_map:
        #     heapq.heappush(min_heap, (hash_map[key], key))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # while min_heap:
        #     result.append(heapq.heappop(min_heap)[1])

        # return result


