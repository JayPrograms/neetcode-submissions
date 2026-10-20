class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()

        #put all 0s into a queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        #bfs to set up queue of valid spacse
        def bfs(r, c):
            #conditions
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return
            
            visited.add((r, c))
            q.append([r, c])

        #do a multi src bfs from each 0, increamanet spaces by 1 for each iteration of bfs
        dist = 0
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1

