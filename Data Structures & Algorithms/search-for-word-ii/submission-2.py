class Solution:
    class Trie:
        def __init__(self):
            self.children = {}
            self.word = None

    def buildTrie(self, words):
        root = self.Trie()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = self.Trie()
                node = node.children[c]
            node.word = word
        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        root = self.buildTrie(words)
        rc = []

        def dfs(r, c, board, root):
            if board[r][c] not in root.children:
                return

            ch = board[r][c]
            board[r][c] = "#"
            if root.children[ch].word:
                rc.append(root.children[ch].word)
                root.children[ch].word = None

            if r > 0:
                dfs(r-1, c, board, root.children[ch])
            if r < rows-1:
                dfs(r+1, c, board, root.children[ch])
            if c > 0:
                dfs(r, c-1, board, root.children[ch])
            if c < cols-1:
                dfs(r, c+1, board, root.children[ch])

            board[r][c] = ch

        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, board, root)

        return rc
            








        