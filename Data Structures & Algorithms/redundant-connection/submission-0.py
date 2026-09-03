class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.parent[n]:
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

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        re = None
        for e in edges:
            n1 = e[0]
            n2 = e[1]
            rc = uf.union(n1, n2)
            if rc == False:
                re = [n1, n2]
        
        return re
        