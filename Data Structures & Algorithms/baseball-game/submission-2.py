class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        n = len(operations)
        for i in range(n):
            op = operations[i]
            match op:
                case '+':
                    p0 = score[-1]
                    p1 = score[-2]
                    ps = p0 + p1
                    score.append(int(ps))
                case 'C':
                    score.pop()
                case 'D':
                    p0 = score[-1]
                    ps = 2 * p0
                    score.append(int(ps))
                case _:
                    score.append(int(op))
        return sum(score)