# Create a grading system (A+, A, B+, B, C, Fail)
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade = A+")
elif marks >= 80:
    print("Grade = A")
elif marks >= 70:
    print("Grade = B+")
elif marks >= 60:
    print("Grade = B")
elif marks >= 40:
    print("Grade = C")
else:
    print("Fail")
