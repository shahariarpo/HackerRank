if __name__ == '__main__':
    N = int(input())
    arr = []
    n1 = 0
    n2 = 0
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            n1 = int(command[1])
            n2 = int(command[2])
            arr.insert(n1, n2)
        elif command[0] == 'print':
            print(arr)
        elif command[0] == 'remove':
            n1 = int(command[1])
            arr.remove(n1)
        elif command[0] == 'append':
            n1 = int(command[1])
            arr.append(n1)
        elif command[0] == 'sort':
            arr.sort()
        elif command[0] == 'pop':
            arr.pop()
        elif command[0] == 'reverse':
            arr.reverse()