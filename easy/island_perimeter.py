class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
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
                    
                    
                   
