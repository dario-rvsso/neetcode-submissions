class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L <= R:
            if s[L].isalnum() != True:
                L += 1
                continue
            if s[R].isalnum() != True:
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1

        return True 