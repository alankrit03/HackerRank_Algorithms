for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('Richard')
        continue
    cache = []
    i = count = 0
    power = -1

    while 2 ** (power + 1) <= n:
        power += 1
        if n ^ 2 ** power == n - 2 ** power:
            cache.append(1)

            count += 1
        else:
            cache.append(0)

    player = ['Louise', 'Richard']
    winner = 0

    while True:
        if cache[-1] == 1:
            if count == 1:
                if power % 2 == 0:
                    winner = (winner + 1) % 2
                break
            else:
                count -= 1
                winner = (winner + 1) % 2
        cache.pop()
        power -= 1

    # print(cache,power,count,sep='\n')
    print(player[winner])
