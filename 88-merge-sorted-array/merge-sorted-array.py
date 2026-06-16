class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        real_nums1 = nums1[:m]
        ans = []
        i = j = 0
        while i < len(real_nums1) and j < len(nums2):
            if real_nums1[i] <= nums2[j]:
                ans.append(real_nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        while i < len(real_nums1):
            ans.append(real_nums1[i])
            i += 1
        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        nums1[:] = ans
        

        # # 倒序双指针
        # p1, p2, p = m - 1, n - 1, m + n - 1
        # while p2 >= 0:
        #     if p1 >= 0 and nums1[p1] > nums2[p2]:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     p -= 1
    
        # # Soltion 1:
        # real_nums1 = nums1[0:m]
        # result = []

        # i = 0
        # j = 0
        # while (i != len(real_nums1)) and (j != len(nums2)):
        #     if (real_nums1[i] > nums2[j]):
        #         result.append(nums2[j])
        #         j += 1
        #     else:
        #         result.append(real_nums1[i])
        #         i += 1

        # while i != len(real_nums1):
        #     result.append(real_nums1[i])
        #     i += 1

        # while j != len(nums2):
        #     result.append(nums2[j])
        #     j += 1

        # for i in range(len(nums1)):
        #     nums1[i] = result[i]

        # return None


        # # Solution 2:
        # real_nums1 = nums1[0:m]
        # result = []
        
        # while(len(real_nums1) != 0 and len(nums2) != 0):
        #     if (real_nums1[0] > nums2[0]):
        #         result.append(nums2[0])
        #         nums2.pop(0)
        #     else:
        #         result.append(real_nums1[0])
        #         real_nums1.pop(0)

        # while(len(real_nums1) != 0):
        #     result.append(real_nums1[0])
        #     real_nums1.pop(0)
            
        # while(len(nums2) != 0):
        #     result.append(nums2[0])
        #     nums2.pop(0)

        # for i in range(len(nums1)):
        #     nums1[i] = result[i]

        # return None





        

