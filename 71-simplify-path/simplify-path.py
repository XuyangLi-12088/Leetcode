class Solution:
    def simplifyPath(self, path: str) -> str:
        # 遍历字符串列表的同时，用栈维护遍历过的字符串：
        #     如果当前字符串是空串或者 .，什么也不做（跳过）。  
        #     如果当前字符串不是 ..，那么把字符串入栈。
        #     否则弹出栈顶字符串（前提是栈不为空），模拟返回上一级目录。
        output = []
        path_list = path.split("/")
        print(path_list)
        for seq in path_list:
            if seq == "." or seq == "":
                continue
            if seq != "..":
                output.append(seq)
            if seq == ".." and output:
                output.pop()
                
        return "/" + "/".join(output)

        