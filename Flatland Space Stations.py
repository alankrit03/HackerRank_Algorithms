# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    arr = [0] * n
    curr_station = min(c)

    for i in range(n):
        if i in c:
            curr_station = i
        else:
            arr[i] = abs(i - curr_station)

    for i in range(n - 1, -1, -1):
        if i in c:
            curr_station = i
        else:
            arr[i] = min(arr[i], abs(i - curr_station))

    return max(arr)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = set(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)
