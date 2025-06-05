class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def calc_diff(gene1, gene2):
            diff = 0
            for c1, c2 in zip(gene1, gene2):
                if c1 != c2:
                    diff += 1
            return diff
        
        diff = calc_diff(startGene, endGene)
        
        # diff_bank = float('inf')
        # while diff_bank == 0:
        #     for c1, c2, c3 in zip(startGene, endGene, )

        # from collections import deque
        # q = deque()
        # q.append((startGene, diff))
        # counter = 0

        # while q:
        #     gene, diff = q.popleft()

        #     if gene == endGene:
        #         return counter

        #     counter += 1

        #     for next_gene in bank:
        #         diff1 = calc_diff(gene, next_gene)
        #         diff2 = calc_diff(next_gene, endGene)
        #         if diff1 == 1 and diff2 == diff-1:
        #             q.append((next_gene, diff2))

        from collections import deque
        q = deque()
        q.append((startGene, 0))
        answer = float('inf')
        # counter = 0
        visited = [False] * len(bank)

        while q:
            gene, counter = q.popleft()

            if gene == endGene:
                # answer = min(answer, counter)
                return counter

            for i, next_gene in enumerate(bank):
                diff1 = calc_diff(gene, next_gene)
                if diff1 == 1 and not visited[i]:
                    visited[i] = True
                    q.append((next_gene, counter+1))
                
        return -1