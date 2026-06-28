# Find the largest among three number using if-else
n1 = int(input("Enter no1: "))
n2 = int(input("Enter no2: "))
n3 = int(input("Enter no3: "))
if n1>n2 and n1>n3 :
    print(n1," is Greater. ")
elif n2>n3 :
    print(n2," is Greater. ")
else:
    print(n3," is Greater. ")