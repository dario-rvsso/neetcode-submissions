class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for c in range(numCourses):
            adj[c] = []
        for p in prerequisites:
            adj[p[1]].append(p[0])
        
        topsort = []
        visit = set()
        vpath = set()

        def dfs(src, adj, visit, vpath, topsort):
            if src in vpath:
                return False
            if src in visit:
                return True

            vpath.add(src)
            visit.add(src)

            for node in adj[src]:
                rc = dfs(node, adj, visit, vpath, topsort)
                if rc == False:
                    return False
            vpath.remove(src)
            topsort.append(src)
            return True

        for c in range(numCourses):
            rc = dfs(c, adj, visit, vpath, topsort)
            if rc == False:
                return []
        return topsort[::-1]




