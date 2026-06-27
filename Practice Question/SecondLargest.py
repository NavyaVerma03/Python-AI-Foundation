# Find the second largest among three numbers without  using sorting.
a = int(input("Enter no1: "))
b = int(input("Enter no2: "))
c = int(input("Enter no3: "))
if(a >= b and a <= c) or (a <= b and a >= c):
    print("Second Largest = ", a)
elif(b >= a and b <= c) or (b <= a and b >= c):
    print("second Largest = ", b)
else:
    print("Second Largest = ", c)

