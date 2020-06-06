
# Complete the permutationEquation function below.
def permutationEquation(p):
    cache = {}
    for i in range(len(p)):
        cache[p[i]] = i+1

    # print(cache)
    ans = []

    for i in range(1,len(p)+1):
        ans.append(cache[cache[i]])

    return ans

if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(*result, sep='\n')