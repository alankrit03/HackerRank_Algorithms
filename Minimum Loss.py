n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

myDict = {}
for i in range(n):
    myDict[arr[i]] = i

minCost = 10_000_000_000
nums = sorted(myDict)

for i in range(1, n):
    if (nums[i] - nums[i - 1] < minCost) and (myDict[nums[i]] < myDict[nums[i - 1]]):
        minCost = nums[i] - nums[i - 1]

print(minCost)
