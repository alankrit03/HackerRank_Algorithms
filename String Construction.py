"""
A really simple insight to this problem is that we can copy any substring and paste with zero dollars.

So very easily we can say that the minimum dollars will only be the number of distinct characters in the string.
Because whenever a character repeats itself we can just copy it from behind and paste it again with no charge.

"""


def stringConstruction(s):
    return len(set(s))


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        print(result)
