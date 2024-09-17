from collections import deque

moves = [(1, 1, "\\"), (-1, 1, "/"), (1, -1, "/"), (-1, -1, "\\")]


def zero_one_bfs(start, end, n, m, edges):
    x0, y0 = start
    x1, y1 = end

    dist = [[100000000 for _ in range(m+1)] for _ in range(n+1)]

    queue = deque()
    queue.appendleft((x0, y0))
    dist[x0][y0] = 0

    while queue:
        x, y = queue.popleft()
        if x == x1 and y == y1:
            return dist[x1][y1]
        for dx, dy, shape in moves:
            nx, ny = x+dx, y+dy
            if not (0 <= nx <= n and 0 <= ny <= m):
                continue
            ox, oy = x + min(dx, 0), y + min(dy, 0)
            weight = 0 if edges[ox][oy] == shape else 1

            new_weight = dist[x][y] + weight
            if new_weight < dist[nx][ny]:
                dist[nx][ny] = new_weight
                if weight == 0:
                    queue.appendleft((nx, ny))
                else:
                    queue.append((nx, ny))

    return dist[x1][y1]


def main():
    n, m = map(int, input().split())
    a = input().split()
    if len(a) == 2:
        x0, y0 = map(int, a)
        x1, y1 = map(int, input().split())
    else:
        x0, y0, x1, y1 = map(int, a)


    if (abs(x0-x1) + abs(y0-y1))%2 == 1:
        return -1
    
    edges = [[None for j in range(m)] for i in range(n)]
    for i in range(n):
        row = input()
        for j in range(m):
            edges[i][j] = row[j]

    

    return zero_one_bfs((x0, y0), (x1, y1), n, m, edges)
      

print(main())
