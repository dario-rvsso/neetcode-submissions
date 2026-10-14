class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = {0}
        for stone in stones:
            dp |= {s + stone for s in dp if s + stone <= target}
        
        return total - 2 * max(dp)