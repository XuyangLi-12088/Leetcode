class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        # 跳过前导空格
        i = 0
        while i < n and s[i] == " ":
            i += 1

        # 处理正负号
        op = 1
        if i < n and s[i] in "+-":
            op = 1 if s[i] == "+" else -1
            i += 1

        # 处理数字
        max_n = 2**31 - 1
        min_n = -2**31
        num_set = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        res = 0
        while i < n and s[i] in num_set:
            res = res * 10 + int(s[i])
            if res > max_n:
                return max_n if op == 1 else min_n
            i += 1
        
        return op * res
        

        



        # s1 = ""
        # output = 0
        # num_set = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        # op_set = ("-", "+")
        # for i, c in enumerate(s):
        #     if c in num_set:
        #         s1 += c
        #     elif c in op_set and s1 == "":
        #         s1 += c
        #     elif c == " " and s1 == "":
        #         continue
        #     else:
        #         break
        
        # num_flag = False
        # s2 = ""
        # for i, c in enumerate(s1):
        #     if c in num_set:
        #         if c == "0" and num_flag == False:
        #             continue
        #         num_flag = True
        #     s2 += c

        # if not s2:
        #     return output

        # op = "+"
        # new_s2 = s2
        # if s2[0] in op_set:
        #     op = s2[0]
        #     new_s2 = s2[1:]

        # m = 1
        # if op == "-":
        #     m = -1
        # for i in range(len(new_s2) - 1, -1, -1):
        #     output = output + (int(new_s2[i]) * m)
        #     m *= 10
                    
        # if output < -2**31:
        #     return -2**31
        # if 2**31-1 < output:
        #     return 2**31-1
            
        # return output
