import heapq

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        # Finds the root of x
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Add original indices to edges: [u, v, w, original_index]
        new_edges = [[edges[i][0], edges[i][1], edges[i][2], i] for i in range(len(edges))]
        new_edges.sort(key=lambda x: x[2])

        def get_mst_weight(skip_idx=-1, force_idx=-1):
            uf = UnionFind(n)
            weight = 0
            count = 0
            if force_idx != -1:
                for u, v, w, idx in new_edges:
                    if idx == force_idx:
                        uf.union(u, v)
                        weight += w
                        count += 1
                        break
            for u, v, w, idx in new_edges:
                if idx == skip_idx:
                    continue
                if uf.union(u, v):
                    weight += w
                    count += 1
            return weight if count == n - 1 else float('inf')

        base_weight = get_mst_weight()
        critical = []
        pseudo = []

        for i in range(len(edges)):
            if get_mst_weight(skip_idx=i) > base_weight:
                critical.append(i)
            elif get_mst_weight(force_idx=i) == base_weight:
                pseudo.append(i)

        return [critical, pseudo]