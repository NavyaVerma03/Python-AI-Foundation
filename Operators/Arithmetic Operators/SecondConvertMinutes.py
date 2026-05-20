# Take total seconds and convert into minutes.

seconds = int(input("Enter total seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print("Minutes =", minutes)
print("Remaining Seconds =", remaining_seconds)