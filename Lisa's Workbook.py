
def workbook(n, k, arr):
    if not arr:
        return 0
    page_num=1
    ans = 0

    for x in arr:
        pages=0
        while pages < x:
            if pages+1 <= page_num <= pages+min(x-pages,k):
                ans += 1
            pages += min(x-pages,k)
            page_num += 1
    return ans




if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)
