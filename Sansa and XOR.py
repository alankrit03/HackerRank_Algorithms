# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    n = int(input())
    arr = input().split()

    """If number of elements is even, eventually all the elements will cancel out each other.
    """
    if n % 2 == 0:
        print(0)
        continue

    """Now the ans will be obtained by xor-ing all the elements at odd place.
    The elements will occur odd number of times which can be checked through generating all subarrays
    just for learning purpose. Generating all subarrays is not required for this problem."""
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans ^= int(arr[i])

    print(ans)
