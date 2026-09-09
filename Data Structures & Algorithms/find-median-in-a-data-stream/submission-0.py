import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1*num)
        if self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

        if len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            self.median = -1 * self.maxHeap[0]
        else:
            self.median = (self.minHeap[0] + (-1 * self.maxHeap[0]))/2
        

    def findMedian(self) -> float:
        return self.median
        
        