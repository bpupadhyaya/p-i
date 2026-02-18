"""
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

-For example, for arr = [2,3,4], the median is 3.
-For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
-MedianFinder() initializes the MedianFinder object.
-void addNum(int num) adds the integer num from the data stream to the data structure.
-double findMedian() returns the median of all elements so far. Answers within 10-5 of the
actual answer will be accepted.

Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
-If all integer numbers from the stream are in the range [0, 100], how would you optimize
your solution?
-If 99% of all integer numbers from the stream are in the range [0, 100], how would you
optimize your solution?

Sample Input/Output:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Tag: R304/2935
Tag: 295/2927
"""

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def add_num(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def find_median(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


def main():

    median_finder = MedianFinder()
    median_finder.add_num(1)
    median_finder.add_num(2)
    print(median_finder.find_median())
    median_finder.add_num(3)
    print(median_finder.find_median())


if __name__ == "__main__":
    main()
