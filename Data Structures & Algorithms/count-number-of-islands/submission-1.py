class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(x, y):
            if visited[x][y] or grid[x][y] == '0':
                return
            visited[x][y] = True
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i, j in directions:
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    backtrack(x + i, y + j)
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == '1' and not visited[x][y]:
                    backtrack(x, y)
                    count += 1

        return count