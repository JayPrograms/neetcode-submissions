class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs where we loop through the grid, at each one. keep a set of seen
        seen = set()

        #for each 1 we visit, hit a dfs and add the 1 to seen.
        def dfs(r, c):
            if (
                r < 0 or
                c < 0 or
                r >= len(grid) or
                c >= len(grid[0]) or
                grid[r][c] == "0" or
                (r, c) in seen
            ):
                return
            seen.add((r,c))

            #visit all adjacent nodes:
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        #when looping, skip over the 1 if its seen

        #for each iteration of the loop, we add 1 to island counter
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
        return islands
