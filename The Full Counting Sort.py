def countSort(arr):
    flag = len(arr)//2

    for i in range(flag):
        arr[i][1] = '-'
    for i in range(len(arr)):
        arr[i][0] = int(arr[i][0])

    x = [[] for i in range(100)]
    # print(x)
    # print(arr)
    for i in range(len(arr)):
        x[arr[i][0]].append(arr[i][1])

    for i in range(100):
        if x[i]:
            print(*x[i] , sep=' ',end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)