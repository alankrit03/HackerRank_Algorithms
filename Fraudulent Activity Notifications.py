from statistics import median

n, d = map(int, input().split())

arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

notification = 0

for i in range(d, n):
    if arr[i] >= 2 * median(arr[i - d:i]):
        notification += 1

print(notification)
