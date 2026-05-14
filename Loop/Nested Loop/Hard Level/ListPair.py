# Generate pairs from two lists and skip even sum pairs

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1:

    for j in list2:

        if (i + j) % 2 == 0:
            continue

        print(i, j)