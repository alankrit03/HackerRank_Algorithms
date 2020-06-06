from collections import Counter

def pickingNumbers(a):
    # Write your code here
    c = Counter(a)
    a = set(a)

    ans = 0
    for x in a:
        ans = max(ans, c[x]+max(c[x-1], c[x+1]))

    return ans
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)