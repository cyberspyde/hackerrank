def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range(1, n+1):
        print(f"{i:{width}d} "
              f"{i:{width}o} "
              f"{i:{width}X} "
              f"{i:{width}b}"
              )
        


print_formatted(17)