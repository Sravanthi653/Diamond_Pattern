# Pyramid Pattern
height = 5

for i in range(1, height + 1):
    print("*" * i)

print()

# Square Pattern
size = 4
char = "#"

for i in range(size):
    print(char * size)

print()

# Diamond Pattern
width = 5

for i in range(1, width + 1, 2):
    spaces = (width - i) // 2
    print(" " * spaces + "*" * i)

for i in range(width - 2, 0, -2):
    spaces = (width - i) // 2
    print(" " * spaces + "*" * i)