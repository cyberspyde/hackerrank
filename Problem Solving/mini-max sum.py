def miniMaxSum(arr):
    summa = sum(arr)
    MyArray = []
    for i in range(0, len(arr)):
        elementToSkip = arr[i]
        newSum = summa - elementToSkip
        MyArray.append(newSum)
    minSum = min(MyArray)
    maxSum = max(MyArray)
    print(minSum, maxSum)
        

arr = [769082435, 210437958, 673982045, 375809214, 380564127]

miniMaxSum(arr)