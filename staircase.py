def staircase(n):
    i = 1
    while(i <= n):
        print(" " * (n - i) + "#" * i)
        i += 1

n = int(input("Enter the n : "))
staircase(int(n))