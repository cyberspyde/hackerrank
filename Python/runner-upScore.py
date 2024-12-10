n = int(input())
arr = map(int, input().split())
myArray = set()
for i in arr:
    myArray.add(i)
maxElement = max(myArray)
myArray.remove(maxElement)
runnerUp = max(myArray)
print(runnerUp)