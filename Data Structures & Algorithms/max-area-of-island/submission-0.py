class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visit = set()
        def dfs(row,col):
            if (
                row< 0  or col<0 or row == ROWS or col == COLS
                or grid[row][col] == 0 or (row,col) in visit
            ):
                return 0
            visit.add((row,col))
            return (1+ dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1))
            #visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area,dfs(r,c))
        return area