x, y, z, n = input("Number : ")

allPermutations = [[i, j, k] for i in range(0, int(x)+1) for j in range(0, int(y)+1) for k in range(0, int(z)+1) if i + j + k != int(n)]
print(allPermutations)