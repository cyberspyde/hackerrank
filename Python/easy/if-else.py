n = 24
    
if not (n % 2) and n <= 5 and n >= 2:
    print("Not Weird")
elif not (n % 2) and n <= 20 and n >= 6:
    print("Weird")
elif not (n % 2) and n > 20:
    print("Not Weird")
elif (n % 2):
    print("Weird")