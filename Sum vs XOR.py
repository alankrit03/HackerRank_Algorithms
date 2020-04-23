#!/bin/python3
# Complete the sumXor function below.


def sumXor(n):
    numOfDigits = 0
    i = 1
    factorial = [1]

    while i < n:
        if n ^ i == n + i:
            numOfDigits += 1
            factorial.append(factorial[-1] * numOfDigits)
        i *= 2
    ans = 0

    for i in range(1, numOfDigits + 1):
        ans += factorial[-1] // (factorial[i] * factorial[numOfDigits - i])

    return ans + 1


if __name__ == '__main__':
    n = int(input().strip())

    result = sumXor(n)
    print(result)