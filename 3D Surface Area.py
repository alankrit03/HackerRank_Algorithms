# Complete the surfaceArea function below.
def surfaceArea(A):
    row = len(A)
    col = len(A[0])

    def getright(i, j):
        if j + 1 >= col:
            return 0
        return A[i][j + 1]

    def getleft(i, j):
        if j - 1 < 0:
            return 0
        return A[i][j - 1]

    def getnorth(i, j):
        if i - 1 < 0:
            return 0
        return A[i - 1][j]

    def getsouth(i, j):
        if i + 1 >= row:
            return 0
        return A[i + 1][j]

    ans = 2 * (row * col)

    for i in range(row):
        for j in range(col):
            curr = A[i][j]
            ans += max(curr - getleft(i, j), 0)
            ans += max(curr - getright(i, j), 0)
            ans += max(curr - getnorth(i, j), 0)
            ans += max(curr - getsouth(i, j), 0)

    return ans


if __name__ == '__main__':
    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    print(result)