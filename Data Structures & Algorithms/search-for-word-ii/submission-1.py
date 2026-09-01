class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = None

    def buildTrie(self, words):
        root = self.TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = self.TrieNode()
                node = node.children[c]
            node.word = w
        return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"

            if r > 0:
                dfs(r-1, c, nxt)
            if r < rows - 1:
                dfs(r+1, c, nxt)
            if c > 0:
                dfs(r, c-1, nxt)
            if c < cols - 1:
                dfs(r, c+1, nxt)

            board[r][c] = ch


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
        
