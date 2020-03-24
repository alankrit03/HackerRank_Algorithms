def superDigit(n, k):
    def super_d(x):
        pass
    if int(n)<10:
        return n
    temp = 0
    while n:
        temp += int(n[-1])
        n = n[:-1]

    return superDigit(str(temp*k), 1)

if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)