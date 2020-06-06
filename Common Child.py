# Complete the commonChild function below.
def commonChild(s1, s2):
    col = len(s1) + 1
    row = len(s2) + 1

    dp = [[0] * (col) for i in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)
    print(result)
