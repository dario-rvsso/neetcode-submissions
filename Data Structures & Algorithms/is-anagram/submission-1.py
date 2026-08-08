class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_of_s = {}
        letters_of_t = {}
        for i in range(len(s)):
            if s[i] not in letters_of_s:
                letters_of_s[s[i]] = 1
            else:
                letters_of_s[s[i]] += 1
            if t[i] not in letters_of_t:
                letters_of_t[t[i]] = 1
            else:
                letters_of_t[t[i]] += 1

        return letters_of_s == letters_of_t
