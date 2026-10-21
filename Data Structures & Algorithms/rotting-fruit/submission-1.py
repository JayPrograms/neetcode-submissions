class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi bfs from each rotten banana
        #to know if any fresh fruit are left: when scanning for rotten, have counter for fresh. decrenmeant fresh when it gets rotten. check if counter is 0 at end

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        #add all rotten to a queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1 

                
                

        



            



