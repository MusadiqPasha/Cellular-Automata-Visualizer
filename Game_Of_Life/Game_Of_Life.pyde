import random
global grid, rows, cols, next_grid

rows = 150  # Width of the grid
cols = 150  # Height of the grid
w = 900 // rows  # Cell size

# Neighbor offsets
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def count(grid, x, y):
    count = 0
    for i in range(8):
        nx = (x + dx[i]) % rows
        ny = (y + dy[i]) % cols
        count += grid[nx][ny]
    return count

def setup():
    size(900, 900)
    global grid, next_grid
    grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    next_grid = [[0] * cols for _ in range(rows)]
    #noStroke()

def draw():
    
    global grid, next_grid
    x,y = 0,0
    global grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                fill(0,0,0)
            else:
                fill(255,255,255)
            rect(x, y, w, w)
            x += w
            
        y += w
        x = 0
    
    # Compute next generation
    for i in range(rows):
        for j in range(cols):
            neigh = count(grid, i, j)
            cur = grid[i][j]
            if cur == 0 and neigh == 3:
                next_grid[i][j] = 1
            elif cur == 1 and (neigh < 2 or neigh > 3):
                next_grid[i][j] = 0
            else:
                next_grid[i][j] = cur

    # Swap grids
    grid, next_grid = next_grid, grid
