# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Complete the steadyGene function below.

def steadyGene(gene):

    n = len(gene)
    cache = Counter(A=n // 4, C=n // 4, G=n // 4, T=n // 4)
    cache = Counter(gene) - cache
    l = 0
    for x in cache:
        l += cache[x]

    window = Counter(gene[:l])
    if not bool(cache - window):
        return l
    j = l

    while bool(cache - window):
        window[gene[j]] += 1
        j += 1

    i = 0


    """Here i following loop I have done the sliding window technique.
    And the window here is the Counter which contracts as per required."""
    while j < n and j - i + 1 > l:
        while not bool(cache - (window - Counter([gene[i]]))):
            window -= Counter([gene[i]])
            i += 1
        window -= Counter([gene[i]])
        i += 1
        window[gene[j]] += 1
        j += 1

    while not bool(cache - (window - Counter([gene[i]]))):
        window -= Counter([gene[i]])
        i += 1

    return j - i


if __name__ == '__main__':
    n = int(input())

    gene = input()

    result = steadyGene(gene)

    print(result)
