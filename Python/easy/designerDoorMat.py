# n = 9
# m = 27
# text = "WELCOME"

# for i in range(0, n, 2):
#     print((".|."*(i-1)).center(m, "-"))
# print(text.center(m, "-"))
# for k in range(n-2, -1, -2):
#     print((".|."*(i)).center(m, "-"))

    # Get dimensions and text
n, m = 9, 27  # Adjust these values as needed
text = "WELCOME"

# Top half of the pattern
for i in range(2, n+1, 2):
    pattern = (".|."*(i-1)).center(m, "-")
    print(pattern)

# Middle line with text
print(text.center(m, "-"))

# Bottom half of the pattern (uses a symmetric approach)
for i in range(n-2, -1, -2):
    pattern = (".|."*i).center(m, "-")
    print(pattern)