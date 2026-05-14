# Print pyramid but skip printing star when column equals center
n= int(input("Enter Row: "))
center= n-1
for i in range(n):
    for j in range(2*n-1):
        if j >= center -i and j <= center +i:
            if center ==j :
                print(" ", end="")
            else:
                print("*", end="")
        else:
            print(" ", end="")
    print()