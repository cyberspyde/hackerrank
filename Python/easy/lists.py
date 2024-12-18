if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input().split()
        match command[0]:
            case "insert":
                list.insert(int(command[1]), int(command[2]))
            case "print":
                print(list)
            case "remove":
                list.remove(int(command[1]))
            case "append":
                list.append(int(command[1]))
            case "sort":
                list.sort()
            case "pop":
                list.pop()
            case "reverse":
                list.reverse()