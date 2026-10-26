from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    land.add((i, j))
        
        # Now we know where are the land is

        # We need to choose one at random and explore the ones connected to it 
        # repeatedly do this

        def dfs(curr):
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for i, j in directions:
                if 0 <= curr[0] + i < len(grid) and 0 <= curr[1] + j < len(grid[0]) and (curr[0] + i, curr[1] + j) in land:
                    land.remove((curr[0] + i, curr[1] + j))
                    dfs((curr[0] + i, curr[1] + j))

        islands = 0
        while land:
            src = land.pop()
            islands += 1
            dfs(src)        
        return islands