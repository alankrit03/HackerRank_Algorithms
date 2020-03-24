ans = [0] * 25


def kFactorization(n, A):
    A.sort()

    def rec_fac(multiple, path, n_arr, index):
        global ans
        # print(multiple,path,n_arr)
        if multiple == n:
            if len(ans) > len(path):
                ans = path[:]
            return
        elif multiple > n:
            return

        for i in range(index, n_arr):
            rec_fac(multiple * A[i], path + [multiple * A[i]], n_arr, i)

    rec_fac(1, [1], len(A), 0)
    if ans[0] == 0:
        return [-1]

    return ans


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A[:k])

    print(*result)
