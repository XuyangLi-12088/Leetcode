class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        res = 0
        queue = collections.deque()
        queue.append(startGene)
        bankset = set(bank)
        
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return res
                for i in range(len(gene)):
                    for x in "ACGT":
                        new_gene = gene[:i] + x + gene[i+1:]
                        if new_gene in bankset and new_gene != gene:
                            queue.append(new_gene)
                            bankset.remove(new_gene)

            res += 1

        return -1

