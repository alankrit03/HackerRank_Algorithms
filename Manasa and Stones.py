# Complete the stones function below.
def stones(n, a, b):
    ans = []
    a, b = min(a, b), max(a, b)
    if a == b:
        return [(n - 1) * a]
    for i in range(n):
        ans.append(a * (n - i - 1) + b * i)

    return ans


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        print(*result)