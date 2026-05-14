# Print matrix but stop if row sum become greater than 10
matrix = [
    [1,2,3],
    [4,5,6],
    [2,2,2]
]
for row in matrix:
    if sum(row) > 10:
        print("Row sum exceeded 10")
        break
    for num in row:
        print(num, end=" ")
    print()
