# searching character in a string grid and print its position
grid = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

target = input("Enter character: ")

for i, row in enumerate(grid):

    for j, ch in enumerate(row):

        if ch == target:
            print("Found at", i, j)
