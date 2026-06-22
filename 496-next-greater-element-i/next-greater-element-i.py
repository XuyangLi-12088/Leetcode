class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Monotonic Stack：
        output = []
        stack = []
        hash_map = {}
        for n in nums2:
            pop_n = None
            while stack and n >= stack[-1]:
                pop_n = stack.pop()
                hash_map[pop_n] = n
            stack.append(n)

        for n in nums1:
            if n in hash_map:
                output.append(hash_map[n])
            else:
                output.append(-1)

        return output


            

            



        # # Two stack solution
        # output = []
        # stack = []
        # temp = []

        # for i in nums2:
        #     stack.append(i)

        # for i in nums1:
        #     max = -1
        #     while stack[-1] != i:
        #         pop_num = stack.pop()
        #         if pop_num > i:
        #             max = pop_num
        #         temp.append(pop_num)
        #     output.append(max)

        #     while len(temp) != 0:
        #         stack.append(temp.pop())
            
        # return output


        # # Hash Table + Stack Solution
        # output = []
        # hash_table = {}
        # stack = []

        # for n in nums2:
        #     if (len(stack) != 0):
        #         while len(stack) != 0 and (n > stack[-1]):
        #             hash_table[stack.pop()] = n
        #         stack.append(n)
        #     else:
        #         stack.append(n)
        
        # while len(stack) != 0:
        #     hash_table[stack.pop()] = -1

        # for n in nums1:
        #     output.append(hash_table[n])

        # return output