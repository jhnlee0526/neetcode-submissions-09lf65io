class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        # Sorting
        #   time : O(n logn)
        #   space: O(n)

        self.data.sort()    # O(n log n)
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        elif n % 2 == 0:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2