class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heap = [0]
        for i in range(len(nums)):
            heap.append(nums[i])
            y = (len(heap) - 1)//2
            j = len(heap) - 1
            while y > 0 and heap[y] > heap[j]:
                tmp = heap[y]
                heap[y] = heap[j]
                heap[j] = tmp
                j = y
                y = y//2

            if len(heap) > k + 1:
                heap[1] = heap.pop()
                y = 1
                while True:
                    j = 2 * y
                    if j + 1 < len(heap) and heap[j+1] < heap[j]:
                        j = j + 1
                    if j < len(heap) and heap[y] > heap[j]:
                        tmp = heap[y]
                        heap[y] = heap[j]
                        heap[j] = tmp
                        y = j
                    else:
                        break

        self.heap = heap
        

    def add(self, val: int) -> int:
        self.heap.append(val)
        y = (len(self.heap) - 1)//2
        j = len(self.heap) - 1
        while y > 0 and self.heap[y] > self.heap[j]:
            tmp = self.heap[y]
            self.heap[y] = self.heap[j]
            self.heap[j] = tmp
            j = y
            y = y//2

        if len(self.heap) > self.k + 1:
            self.heap[1] = self.heap.pop()
            y = 1
            while True:
                j = 2 * y
                if j + 1 < len(self.heap) and self.heap[j+1] < self.heap[j]:
                    j = j + 1
                if j < len(self.heap) and self.heap[y] > self.heap[j]:
                    tmp = self.heap[y]
                    self.heap[y] = self.heap[j]
                    self.heap[j] = tmp
                    y = j
                else:
                    break

        return self.heap[1]