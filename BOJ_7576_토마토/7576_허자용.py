import collections

green = 0
q = collections.deque()
box = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def isOutOfBox(r, c):
    if r == -1 or r == N or c == -1 or c == M:
        return True
    else:
        return False


def ripe(r, c, date):
    for i in range(4):
        if isOutOfBox(r + dr[i], c + dc[i]):
            continue
        elif box[r + dr[i]][c + dc[i]] == 0:
            box[r + dr[i]][c + dc[i]] = 1
            global green
            green -= 1
            q.append(r + dr[i])
            q.append(c + dc[i])
            q.append(date)


[M, N] = list(map(int, input().split()))

for i in range(N):
    templist = list(map(int,input().split()))
    box.append(templist)
    for j in range(M):
        if not box[i][j]:
            green += 1
        if box[i][j] == 1:
            q.append(i)
            q.append(j)
            q.append(0)

if not green:
    print(0)

else:
    while(q):
        temp_r = q.popleft()
        temp_c = q.popleft()
        temp_date = q.popleft()
        ripe(temp_r, temp_c, temp_date + 1)

    if green:
        print(-1)

    else:
        print(temp_date)