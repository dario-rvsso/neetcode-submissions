class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def heapify(stones):
            stones.insert(0, 0)
            curr = (len(stones) - 1) // 2
            while curr > 0:
                i = curr
                while True:
                    largest = i
                    left = 2 * i
                    right = 2 * i + 1
                    if left < len(stones) and stones[left] > stones[largest]:
                        largest = left
                    if right < len(stones) and stones[right] > stones[largest]:
                        largest = right
                    if largest != i:
                        stones[i], stones[largest] = stones[largest], stones[i]
                        i = largest
                    else:
                        break
                curr -= 1
            return stones

        def heappop(stones):
            if len(stones) <= 1:
                return 0, [0]
            if len(stones) == 2:
                return stones.pop(), stones
            rc = stones[1]
            stones[1] = stones.pop()
            i = 1
            while True:
                largest = i
                left = 2 * i
                right = 2 * i + 1
                if left < len(stones) and stones[left] > stones[largest]:
                    largest = left
                if right < len(stones) and stones[right] > stones[largest]:
                    largest = right
                if largest != i:
                    stones[i], stones[largest] = stones[largest], stones[i]
                    i = largest
                else:
                    break
            return rc, stones

        def heapadd(stones, val):
            stones.append(val)
            curr = len(stones) - 1
            i = curr // 2
            while i > 0:
                if stones[curr] > stones[i]:
                    stones[i], stones[curr] = stones[curr], stones[i]
                    curr = i
                    i = curr // 2
                else:
                    break
            return stones
        
        stones = heapify(stones)
        while len(stones) > 2:
            x, stones = heappop(stones)
            y, stones = heappop(stones)
            diff = abs(x - y)
            if diff > 0:
                stones = heapadd(stones, diff)

        if len(stones) == 2:
            return stones[1]
        else:
            return 0


