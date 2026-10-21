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


        #do a multi src bfs from each 0, increamanet spaces by 1 for each iteration of bfs
        dist = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if row not in range(ROWS) or col not in range(COLS) or grid[row][col] == -1 or (row, col) in visited:
                        continue
                    visited.add((row, col))
                    q.append((row, col))
                                  



            dist += 1

