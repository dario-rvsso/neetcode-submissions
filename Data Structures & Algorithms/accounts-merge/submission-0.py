class UnionFind:
    def __init__(self, accounts):
        self.parent = {}
        self.rank = {}
        self.owner = {}

        for a in accounts:
            owner = a[0] 
            for i in range(1, len(a)):
                e = a[i]
                self.parent[e] = e
                self.rank[e] = 0
                self.owner[e] = owner

    def find(self, email):
        if email != self.parent[email]:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, e1, e2):
        p1, p2 = self.find(e1), self.find(e2)
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(accounts)
        groups = {}

        for a in accounts:
            n1 = a[1]
            for i in range(2, len(a)):
                n2 = a[i]
                uf.union(n1, n2)

        # Groups logic 
        for email in uf.parent:
            root = uf.find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        # Build final result
        result = []
        for root, emails in groups.items():
            name = uf.owner[root]
            emails.sort()
            result.append([name] + emails)

        return result
        





        