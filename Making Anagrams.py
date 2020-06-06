from collections import Counter


# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    mask = 'abcdefghijklmnopqrstuvwxyz'

    s1 = Counter(s1)
    s2 = Counter(s2)

    ans = 0
    for x in mask:
        ans += abs(s1[x] - s2[x])

    return ans


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)
