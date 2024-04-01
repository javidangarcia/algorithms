class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        if abs(len(self.small) - len(self.large)) > 1 or (self.small and self.large and self.small[0] * -1 > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
            if abs(len(self.small) - len(self.large)) > 1:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.small[0] * -1 + self.large[0]) / 2

# Time: O(log(n)) and O(1)
# Space: O(n)