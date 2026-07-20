class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # k = 0
        # n = math.floor(len(nums)/2)

        # dict = {}

        # for num in nums:
        #     if num in dict:
        #         dict[num] += 1
        #     else:
        #         dict[num] = 1

        # for key in dict:
        #     if (dict[key] > n):
        #         k = key
        #         break
        
        # return k

        # nums.sort()
        # n = len(nums)
        # return nums[n//2]

        ans = hp = 0
        for x in nums:
            if hp == 0:
                ans , hp = x, 1
            else:
                if ans == x:
                    hp += 1
                else:
                    hp -= 1
        return ans
        