class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def filler(image, sr, sc, inicolor, visited):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return visited
            if image[sr][sc] != inicolor or (sr, sc) in visited:
                return visited
            
            visited.add((sr, sc))

            visited.union(filler(image, sr-1, sc, inicolor, visited ))
            visited.union(filler(image, sr+1, sc, inicolor, visited ))
            visited.union(filler(image, sr, sc-1, inicolor, visited ))
            visited.union(filler(image, sr, sc+1, inicolor, visited ))

            return visited
        
        visited = set()
        inicolor = image[sr][sc]
        visited.union(filler(image, sr, sc, inicolor, visited))

        for v in visited:
            image[v[0]][v[1]] = color

        return image
            

