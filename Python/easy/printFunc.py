def printFunc(n):
    myStr = ""
    for i in range(1, n+1):
        myStr += str(i)
    print(myStr)

n = int(input("Enter number: "))
printFunc(n)