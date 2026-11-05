class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        count = Counter(tasks)

        #create a max heap for frequency of each task
        #create a Q
        maxheap = [-s for s in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque() # [-cnt, time+n]
        while maxheap or q:
            time = time +1 
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
                
        return time