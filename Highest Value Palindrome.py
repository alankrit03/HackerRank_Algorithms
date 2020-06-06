# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    arr = [0] * n

    if k >= n:
        return ''.join(['9'] * n)

    for i in range(n):
        arr[i] = int(s[i])

    required_changes = 0
    for i in range(n // 2):
        if arr[i] != arr[-i - 1]:
            required_changes += 1

    if required_changes > k:
        return -1

    double_allowed = k - required_changes

    for i in range(n // 2):
        if arr[i] != arr[-i - 1]:
            if arr[i] == 9 or arr[-i - 1] == 9:
                arr[-i - 1] = 9
                arr[i] = 9
                k -= 1
            elif double_allowed:
                arr[-i - 1] = 9
                arr[i] = 9
                k -= 2
                double_allowed -= 1
            else:
                if arr[i] > arr[-i - 1]:
                    arr[-i - 1] = arr[i]
                else:
                    arr[i] = arr[-i - 1]
                k -= 1

    for i in range(n // 2):
        if arr[i] != 9 and k > 1:
            arr[i] = 9
            arr[-i - 1] = 9
            k -= 2
        if k < 2:
            break

    if n % 2 and k:
        arr[n // 2] = 9

    for i in range(n):
        arr[i] = str(arr[i])

    return ''.join(arr)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)
    print(result)