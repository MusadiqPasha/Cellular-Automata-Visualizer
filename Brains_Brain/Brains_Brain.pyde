import random
global grid, rows, cols, next_grid

rows = 100  # Width of the grid
cols = 100  # Height of the grid
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
            if grid[i][j] == 1:  # On
                fill(0, 0, 255)  # Blue for 'on'
            elif grid[i][j] == 2:  # Dying
                fill(255, 0, 0)  # Red for 'dying'
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

            if curr == 0 and neigh == 2:
                next_grid[i][j] = 1  # Off -> On if exactly 2 neighbors are 'on'
            elif curr == 1:
                next_grid[i][j] = 2  # On -> Dying
            elif curr == 2:
                next_grid[i][j] = 0  # Dying -> Off
            else:
                next_grid[i][j] = curr  # Retain current state
    # Swap grids
    grid, next_grid = next_grid, grid
