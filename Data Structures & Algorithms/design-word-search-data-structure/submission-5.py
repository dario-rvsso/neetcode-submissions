class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self
        rc = False
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for trie in curr.children.values():
                    if trie.search(word[i+1:]):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        
        return curr.word

        
