class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        output = []
        path = []
        def dfs(i, rest_s):
            if i == 4:
                output.append(".".join(path.copy()))
                return
            
            if i == 3:
                if len(rest_s) >= 4 or len(rest_s) == 0:
                    return
                if 255 < int(rest_s):
                    return
                if rest_s[0] == "0" and len(rest_s) != 1:
                    return
                path.append(rest_s)
                dfs(i+1, rest_s)
                path.pop()

            else:
                for j in range(0, 3):
                    p = rest_s[:j+1]
                    if len(p) >= 4 or len(p) == 0:
                        return
                    if 255 < int(p):
                        return
                    if p[0] == "0" and len(p) != 1:
                        return
                    path.append(p)
                    dfs(i+1, rest_s[j+1:])
                    path.pop()

        dfs(0, s)
        return output

