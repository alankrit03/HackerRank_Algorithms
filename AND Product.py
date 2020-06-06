def rangeBitwiseAnd(m: int, n: int) -> int:
    if not m:
        return 0

    if n - m < 2:
        return m & n

    power = 1
    while power <= n:
        if m < power <= n:
            return 0
        power *= 2

    power //= 2
    ans = 0
    temp = m

    while power >= n - m + 1:
        if temp >= power and power & m and power & n:
            ans += power
            temp = temp - power
        power //= 2

    return ans


def andProduct(a, b):
    return rangeBitwiseAnd(a, b)


if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)
        print(result)