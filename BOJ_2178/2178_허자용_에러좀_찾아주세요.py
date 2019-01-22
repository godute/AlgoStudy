import queue

q = queue.Queue()
land = []
visited = []
ans = 0


def push(n, m, dist):
    visited[n][m] = True
    q.put(n)
    q.put(m)
    q.put(dist)
    return


def go(n, m, dist):
    # up
    if n and not(visited[n - 1][m]) and land[n - 1][m] == '1':
        push(n - 1, m, dist + 1)
    # down
    if n != N - 1 and not(visited[n + 1][m]) and land[n + 1][m] == '1':
        push(n + 1, m, dist + 1)
    # left
    if m and not(visited[n][m - 1] and land[n][m - 1]) == '1':
        push(n, m - 1, dist + 1)
    # right
    if m != M - 1 and not(visited[n][m + 1]) and land[n][m + 1] == '1':
        push(n, m + 1, dist + 1)
    return


[N, M] = list(map(int, input().split()))

for i in range(N):
    land.append(input())
    visited.append([0]*M)

push(0, 0, 1)

while (q.qsize()):
    temprow = q.get()
    tempcol = q.get()
    tempdist = q.get()

    if (temprow == N - 1 and tempcol == M - 1):
        ans = tempdist
        break
    else:
        go(temprow, tempcol, tempdist)

print(ans)
