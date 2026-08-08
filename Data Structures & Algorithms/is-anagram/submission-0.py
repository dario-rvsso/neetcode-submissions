class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        for l in t:
            if l not in letters:
                return False
            else:
                letters[l] -= 1
                if letters[l] < 0:
                    return False
        residual = letters.values()
        for r in residual:
            if r != 0:
                return False
        return True