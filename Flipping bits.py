i = 1
mask = 0
for _ in range(32):
    mask += i
    i *= 2
# Complete the flippingBits function below.
def flippingBits(n):
    n = n^mask
    return n
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print(result)