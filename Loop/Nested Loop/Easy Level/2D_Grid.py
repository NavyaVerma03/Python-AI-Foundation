# Search for number in 2D grid and break when found
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

found = False

for row in grid:
    for num in row:
        if num == 5:
            print("Found")
            found = True
            break
    if found:
        break