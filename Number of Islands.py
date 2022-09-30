Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:   
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        visited_islands = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited_islands:
                    self.dfs(grid, r, c, visited_islands, rows, cols)
                    count += 1
                
        return count
    
    def dfs(self, grid, r, c, visited_islands, rows, cols):
        stack = []
        stack.append((r, c))
        
        while stack:
            island_r, island_c = stack.pop()
                    
            if (island_r, island_c) in visited_islands:
                continue
            visited_islands.add((island_r, island_c))
                                        
            potential_neighbours = [(island_r-1, island_c), (island_r+1, island_c), (island_r, island_c-1), (island_r, island_c+1)]
            for neighbour in potential_neighbours:
                neighbour_r, neighbour_c = neighbour
                        
                if self.is_an_island(grid, neighbour_r, neighbour_c, rows, cols):
                    stack.append(neighbour)        
    
    def is_an_island(self, grid, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"
