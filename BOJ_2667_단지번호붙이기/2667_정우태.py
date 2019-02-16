import collections

def boundary(i, j): #범위를 벗어나는지 체크하는 함수
    return i >= 0 and i < N and j >= 0 and j < N

def bfs():  # 반환값 :bfs로 방문한 총 개수 = 해당 단지의 크기
    res = 0
    while len(q) > 0:
        i, j = q.popleft()
        res += 1
        for k in d:
            ni = i + k[0]
            nj = j + k[1]
            if boundary(ni, nj) and Map[ni][nj] is 1 and not(visited[ni][nj]):
                visited[ni][nj] = True
                q.append([ni, nj])
    return res
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = collections.deque()

N = int(input())
Map = list()
visited = list()
result = list()
cnt = 0     #총 단지의 개수
for i in range(N):
    Map.append([int(i) for i in input()])
    visited.append([False]*N)
for i in range(N):
    for j in range(N):
        if Map[i][j] is 1 and not(visited[i][j]):
            visited[i][j] = True
            q.append([i, j])
            result.append(bfs())
            cnt += 1    #bfs한번 끝날때마다, 단지 개수 +1
result.sort()
print(cnt)
for i in result:
    print(i)

