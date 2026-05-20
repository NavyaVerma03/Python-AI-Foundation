# Longest Word
s = input("Enter Sentance: ")

words = s.split()

longest = max(words, key=len)

print(longest)