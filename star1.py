# Star Nested Loop

row = 7
# Outer Loop
for i in range(1, row + 1):
    # Inner Loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
