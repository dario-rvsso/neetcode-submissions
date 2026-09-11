class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def helper(i, digits, curComb, totComb):
            if len(curComb) == len(digits):
                totComb.append("".join(curComb.copy()))
                return
            if i >= len(digits):
                return
            
            for j in range(i, len(digits)):
                d = digits[j]
                if d == '2':
                    for c in ['a', 'b', 'c']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '3':
                    for c in ['d', 'e', 'f']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '4':
                    for c in ['g', 'h', 'i']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '5':
                    for c in ['j', 'k', 'l']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '6':
                    for c in ['m', 'n', 'o']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '7':
                    for c in ['p', 'q', 'r', 's']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '8':
                    for c in ['t', 'u', 'v']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                if d == '9':
                    for c in ['w', 'x', 'y', 'z']:
                        curComb.append(c)
                        helper(j+1, digits, curComb, totComb)
                        curComb.pop()
                    

        curComb = []
        totComb = []
        i = 0

        if len(digits) == 0:
            return []

        helper(i, digits, curComb, totComb)
        return totComb