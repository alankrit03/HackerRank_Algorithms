

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    cache = {}
    ans = 0
    n = len(s)

    for i in range(1, n + 1):
        for j in range(i):
            new_s = ''.join(sorted(s[j:i]))

            if new_s in cache:
                ans += cache[new_s]
                print(new_s, cache[new_s])
                cache[new_s] += 1
            else:
                print(new_s)
                cache[new_s] = 1

    return ans


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)