class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #extending grid in all directions by 0
        #THis section can be replaced by a more complex if statement while iterating through dirs
        #How would it affect time complexity?
        cols = len(grid[0])
        rows = len(grid)
        emptyRow = [0 for i in range(cols +2)]
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid = [emptyRow] + grid + [emptyRow]
        
        visited = set()
        res = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val and (x, y) not in visited:
                    area = 0
                    stack = [(x, y)]
                    visited.add((x, y))
                    
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        dirs = [[r-1,c], [r+1,c], [r, c+1], [r, c-1]]
                        
                        for row2, col2 in dirs:
                            if grid[row2][col2] and (row2, col2) not in visited:
                                stack.append((row2, col2))
                                visited.add((row2, col2))
                    
                    res = max(res, area)
                    
                    
        return res
                    
                            
