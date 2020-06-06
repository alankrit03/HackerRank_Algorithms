from collections import Counter


# Complete the anagram function below.
def anagram(s):
    n = len(s)
    if n % 2:
        return -1

    a = Counter(s[:n // 2])
    b = Counter(s[n // 2:])

    a = a - b
    ans = 0

    for x in a.values():
        ans += x

    return ans


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)