# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n

        while s <= e and e > 0:
            pick = (s + e) // 2
            rc = guess(pick)
            if rc == 0:
                return pick
            elif rc < 0:
                e = pick - 1
            else:
                s = pick + 1
        return -1 