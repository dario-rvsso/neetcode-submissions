class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        letters = []

        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = []
                    letters.append(c)

        for i in range(len(words)-1):
            j = i + 1
            w1 = words[i]
            w2 = words[j]
            if (len(w1) > len(w2)) and w1.startswith(w2):
                return ""
            for c in range(min(len(w1), len(w2))):
                if w1[c] != w2[c]:
                    adj[w2[c]].append(w1[c])
                    break
        
        topsort = []
        visit = set()
        vpath = set()

        def dfs(src, adj, visit, vpath, topsort):
            if src in vpath:
                return False
            if src in visit:
                return True
            
            visit.add(src)
            vpath.add(src)

            for node in adj[src]:
                rc = dfs(node, adj, visit, vpath, topsort)
                if rc == False:
                    topsort = []
                    return False
            
            vpath.remove(src)
            topsort.append(src)
            return True
        
        rc = False
        for l in letters:
            rc = dfs(l, adj, visit, vpath, topsort)
            if rc == False:
                return ""
        
        #topsort = topsort[::-1]
        return "".join(topsort)








