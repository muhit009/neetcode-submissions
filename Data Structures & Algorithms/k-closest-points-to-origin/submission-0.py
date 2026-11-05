class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a max heap of size k
        # make the max heap to min heap (neagtive squared distance)
        # if heap exceed k, pop the furthest one
        maxHeap = []
        for x,y in points:
            dist = -(x**2 +y**2)
            heapq.heappush(maxHeap, [dist,x,y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res