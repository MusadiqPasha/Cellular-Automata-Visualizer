import random
global grid, rows, cols, next_grid

rows = 300  # Width of the grid
cols = 300  # Height of the grid
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
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # On
                fill(0, 255, 0)  # Green for 'on'
            else:  # Off
                fill(255, 255, 255)  # White for 'off'
            rect(x, y, w, w)
            x += w
        y += w
        x = 0
    
    # Compute next generation
    for i in range(rows):
        for j in range(cols):
            neigh = count(grid, i, j)
            curr = grid[i][j]

            if curr == 0 and neigh in (5,6,7):
                next_grid[i][j] = 1  # Off -> On (Birth)
            elif curr == 1 and neigh in (4, 5, 6, 7):
                next_grid[i][j] = 1  # On -> On (Survival)
            else:
                next_grid[i][j] = 0  # All other cases -> Off (Death)
    # Swap grids
    grid, next_grid = next_grid, grid
