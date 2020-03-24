"""NOT YET COMPLETE SOLUTION"""


def happyLadybugs(b):
    #
    # Write your code here.
    #
    data = sorted(list(b))
    n = len(data)
    if n==1:
        if data[0] == "_":
            return 'YES'
        else:return 'NO'
    i = 0
    while i < n:
        if i == 0:
            if data[i] != data[i+1]:
                return 'NO'
        elif i == n-1:
            if data[i] != data[i-1] and data[i]!='_':
                return 'NO'
        else:
            if data[i] != data[i-1] and data[i]!=data[i+1]:
                return 'NO'
        i += 1

    # if ''.join(data) == b or data[-1]=='_':
    #     return 'YES'
    return 'YES'


if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(b,result)
