class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
    
        # Min-heap of all projects sorted by capital needed
        capital_heap = []
        for i in range(n):
            heapq.heappush(capital_heap, (capital[i], profits[i]))
        
        # Max-heap of affordable projects sorted by profit
        profit_heap = []
        
        for _ in range(k):
            # Move all projects we can now afford to profit_heap
            while capital_heap and capital_heap[0][0] <= w:
                cap, profit = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, (-profit, cap))
            
            if not profit_heap:
                break  # No affordable projects left
            
            # Take the highest profit project
            neg_profit, _ = heapq.heappop(profit_heap)
            w += -neg_profit
        
        return w
        