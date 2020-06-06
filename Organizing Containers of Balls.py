# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    boxes = [0] * n
    types = [0] * n

    for i in range(n):
        for j in range(n):
            boxes[i] += container[i][j]
            types[j] += container[i][j]

    boxes.sort()
    types.sort()

    for i in range(n):
        if boxes[i] != types[i]:
            return 'Impossible'
    return 'Possible'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)