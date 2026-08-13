class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycles(node, nodes, visited, safe):
            if node in visited:
                return True

            if node in safe:
                return False

            cycles = False
            visited.add(node)
    
            for n in nodes[node]:
                cycles = hasCycles(n, nodes, visited, safe)
                if cycles == True:
                    return cycles

            visited.remove(node)
            safe.add(node)
            
            return cycles


        cycles = False
        visited = set()
        safe = set()
        nodes = {}

        for i in range(numCourses):
            nodes[i] = []
        for c,p in prerequisites:
            nodes[c].append(p)
        
        for k in nodes:
            cycles = hasCycles(k, nodes, visited, safe)
            if cycles == True:
                return False
        
        return True
