from collections import Counter
def gameOfThrones(s):
    set_s = (set(s))
    c = Counter(s)
    odd_allowed = 1 if len(s)%2 else 0

    for x in set_s:
        if c[x]%2:
            if not odd_allowed:
                return 'NO'
            odd_allowed -= 1
    return 'YES'

if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)
