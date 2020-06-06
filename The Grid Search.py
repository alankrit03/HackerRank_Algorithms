
# Complete the gridSearch function below.
def gridSearch(G, P, R, C, r, c):

    for i in range(R-r+1):
        for j in range(C-c+1):
            if G[i][j]==P[0][0]:
                for z in range(r):
                    if G[z+i][j:j+c]!=P[z]:
                        break
                else:return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P, R, C, r, c)

        print(result)