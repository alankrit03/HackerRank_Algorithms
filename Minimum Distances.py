
def minimumDistances(a):
    cache = {}
    n = len(a)
    ans = n+2

    for i in range(n):
        if a[i] in cache:
            ans = min(ans, i-cache[a[i]])
        cache[a[i]] = i

    if ans==n+2:
        return -1
    return ans

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)