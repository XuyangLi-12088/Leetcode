class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # {"johnsmith@mail.com": [0, 1], "john_newyork@mail.com": [0], "john00@mail.com": [1], "mary@mail.com": [2], "johnnybravo@mail.com": [3]}
        hash_map = {}
        for i in range(0, len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in hash_map:
                    hash_map[email].append(i)
                else:
                    hash_map[email] = [i]
        
        def dfs(i: int):
            vis[i] = True
            for email in accounts[i][1:]:   # 遍历 i 的所有邮箱地址
                if email in email_set:
                    continue
                email_set.add(email)
                for j in hash_map[email]:   # 遍历所有包含该邮箱地址的账户下标 j
                    if not vis[j]:  # j 没有访问过
                        dfs(j)



        ans = []
        vis = [False] * len(accounts)
        for i, b in enumerate(vis):
            if not b:   # i 没有访问过
                email_set = set()   # 用于收集 DFS 中访问到的邮箱地址
                dfs(i)
                ans.append([accounts[i][0]] + sorted(email_set))
        return ans



        return

