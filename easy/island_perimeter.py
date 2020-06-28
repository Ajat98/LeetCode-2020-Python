class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #Optimal time solution
        s, m = len(grid), len(grid[0])
        ans = 0
        for x in range(s):
            for y in range(m):
                if grid[x][y] == 1:
                    ans += 4
                    if x < s - 1 and grid[x+1][y] == 1:
                        ans -= 2
                    if y < m - 1 and grid[x][y+1] == 1:
                        ans -= 2

        return ans
        
        
        '''
        #Concise solution
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for k in [(-1, 0), (0, -1), (1, 0), (0, -1)]:
                        if i+k[0] < 0 or i+k[0] >=rows or j+k[1] < 0 or j+k[1] >= cols or grid[i+k[0]][j+k[1]] == 0:
                            count += 1
        return count
        '''
        '''
        ORIGINAL MESSY SOLUTION
        cols = len(grid[0])
        rows = len(grid)
        edges = 0
        tile_count = 0
        for i in range(rows):
            for j in range(cols):
                tile = grid[i][j]
                if tile == 1:
                    tile_count += 1
                    pos = [i, j]
                    
                    
                    #print(pos)
                    dirs = [ [i+1, j], [i-1, j], [i, j+1], [i, j-1] ]
                    tile_edges = 4
                    for d in dirs:
                        try:
                            loc = grid[d[0]][d[1]]
                            if loc == 1 and d[0] >= 0 and d[1] >= 0:  #fixes issue of slicing backwards with negative int
                                tile_edges -= 1
                                #print('minus 1', d)
                        except Exception as e:
                            pass
                    #print(pos, tile_edges)
                    edges += tile_edges
        
        return edges
        '''            
                    
                    
                   
