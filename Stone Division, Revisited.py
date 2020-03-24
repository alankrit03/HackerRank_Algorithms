def stoneDivision(n, s, cache):
    if n<2:
        return 0
    if cache.get(n):
        return cache[n]
    max_ = 0
    for x in s:
        if n>x and n%x == 0:
            ele = n//x * (stoneDivision(x, s, cache))
            if ele >= max_:
                max_ = ele+1
    cache[n] = max_
    return max_


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])
        cache={}
        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s, cache)

        print(result)