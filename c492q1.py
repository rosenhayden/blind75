class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        curSmallest = 101 # cheeky bc bounds
        smallestIdx = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and curSmallest > capacity[i]:
                curSmallest = capacity[i]
                smallestIdx = i
        if smallestIdx == -1:
            return -1
        else:
            return smallestIdx
