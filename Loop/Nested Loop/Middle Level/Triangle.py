# Print Triangle but use pass when number is divisible by 4
for i in range (1,6):
    for j in range (1, i+1):
        if j % 4 == 0:
           pass
        print(j, end=" ")
    print()
