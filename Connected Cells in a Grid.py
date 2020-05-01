# Enter your code here. Read input from STDIN. Print output to STDOUT

row = int(input())
col = int(input())

grid = []

for i in range(row):
    grid.append(input().split())

# print(*grid)

ans = 0


def bfs(grid, i, j):
    if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
        return 0

    grid[i][j] = '0'

    return 1 + bfs(grid, i - 1, j) + bfs(grid, i + 1, j) + bfs(grid, i, j - 1) + bfs(grid, i, j + 1) + bfs(grid, i + 1,
                                                                                                           j - 1) + bfs(
        grid, i + 1, j + 1) + bfs(grid, i - 1, j + 1) + bfs(grid, i - 1, j - 1)


for i in range(row):
    for j in range(col):
        if grid[i][j] == '1':
            ans = max(ans, bfs(grid, i, j))

print(ans)