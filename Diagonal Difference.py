def solve(arr):
    n = len(arr)
    rDiagonal = 0
    Diagonal = 0    
    
    for i in range(n):
        Diagonal += arr[i][i]
    for i in range(n):
        rDiagonal += arr[i][n-i-1]

    return abs(rDiagonal - Diagonal)

myarray = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]]

print(solve(myarray))