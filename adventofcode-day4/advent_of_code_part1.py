

with open("input.txt") as f:
    grid = f.read().splitlines()

accessible_cells = 0
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
                accessible_cells += 1

print(accessible_cells)