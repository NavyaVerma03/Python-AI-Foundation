# Reverse Words
s = input("Enter string: ")

result = " ".join(s.split()[::-1])

print(result)