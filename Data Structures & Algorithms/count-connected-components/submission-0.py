class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = set()
        uf = UnionFind(n)
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            uf.union(n1, n2)

        for p in uf.parent:
            curr = p
            while uf.parent[curr] != curr:
                curr = uf.find(uf.parent[curr])
            parents.add(curr)

        return len(parents)
        
        