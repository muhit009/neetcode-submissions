class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL =len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        def wave(r,c):
            nonlocal fresh
            if (
                r<0 or r==ROW or c<0 or c==COL or
                (r,c) in visit or grid[r][c] == 0
            ):
                return
            visit.add((r,c))
            q.append([r,c])
            fresh = fresh - 1
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1                    
        t = 0
        while q:
            for i in range(len(q)):

                r,c = q.popleft()
                wave(r+1,c)
                wave(r-1,c)
                wave(r,c+1)
                wave(r,c-1)
            if q:
                t = t+1
        return t if fresh == 0 else -1
