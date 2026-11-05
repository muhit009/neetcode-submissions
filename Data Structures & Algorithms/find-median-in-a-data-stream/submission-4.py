class MedianFinder:

    def __init__(self):
        # large heap: use min
        # small heap: use max
        # heaps can only differ by size 1 
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Step 2: Make sure every num in small <= every num in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2.0
        