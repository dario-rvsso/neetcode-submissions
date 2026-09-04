class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.size = {}
        for e in n:
            self.parent[e] = e
            self.rank[e] = 0
            self.size[e] = 1
    
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
            self.size[p1] += self.size[p2]
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
            self.size[p2] += self.size[p1]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        edges = {}
        maxsize = 0
        for n in nums:
            edges[n] = n

        for n in edges:
            if n-1 in edges:
                uf.union(n-1, n)

        for e in uf.size.values():
            if e > maxsize:
                maxsize = e

        return maxsize
        

            


        