class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd-Warshall / reachability matrix approach or precomputing reachable sets
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            is_prereq[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prereq[i][k] and is_prereq[k][j]:
                        is_prereq[i][j] = True

        return [is_prereq[u][v] for u, v in queries]