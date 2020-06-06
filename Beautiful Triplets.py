from collections import Counter
# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    c = Counter(arr)
    ans = 0

    arr = set(arr)

    for x in arr:
        ans += c[x] * c[x + d] * c[x + 2 * d]

    return ans


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)