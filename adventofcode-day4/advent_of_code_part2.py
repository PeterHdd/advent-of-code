

with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]


accessible_cells = 0

while True:
    to_remove = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count = 0
            if grid[row][col] == "@":
                if col+1 < len(grid[row]) and grid[row][col+1] == "@":
                    count += 1
                if col-1 >= 0 and grid[row][col-1] == "@":
                    count += 1
                if row+1 < len(grid) and grid[row+1][col] == "@":
                    count += 1
                if row-1 >= 0 and grid[row-1][col] == "@":
                    count += 1
                if row-1 >=0 and col-1 >= 0 and grid[row-1][col-1] == "@":
                    count += 1
                if row+1 < len(grid) and col+1 < len(grid[row]) and grid[row+1][col+1] == "@":
                    count += 1
                if row+1 < len(grid) and col-1 >= 0 and grid[row+1][col-1] == "@":
                    count += 1
                if row-1 >= 0 and col+1 < len(grid[row]) and grid[row-1][col+1] == "@":
                    count += 1
                if count < 4:
                    to_remove.append((row, col))
                
    if not to_remove:
        break
    accessible_cells += len(to_remove)    
    for r, c in to_remove:
        grid[r][c] = "."

print(accessible_cells)