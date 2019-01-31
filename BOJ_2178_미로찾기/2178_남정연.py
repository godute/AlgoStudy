n = input()
m = input()
n_index = n - 1
m_index = m - 1

mirolist = []
for i in range(n):
    miro = []
    newm = input()
    for v in newm:
        miro += v
    mirolist.append(miro)


class Node:
    depth = 0

    def __init__(self, depth, i, j):
        self.depth = depth
        self.i = i
        self.j = j


def check(i, j):
    global mirolist
    global visited
    if (mirolist[i][j] == '1') & (visited[i][j] == 0):
        return 1


def visit(i, j):
    global visited
    visited[i][j] = 1
    return visited


visited = []
for i in range(n):
    visited.append([0] * m)
    visited[0][0] = 1
# main
# 너비 우선 탐색
visited = []
for i in range(n):
    visited.append([0] * m)
    visited[0][0] = 1

depth = 0
i = 0
j = 0
q = queue.Queue()
q.put(Node(1, 0, 0))
count = 0
while not q.empty():
    item = q.get_nowait()
    i = item.i
    j = item.j
    depth = item.depth
    if i < n_index:
        if check(i + 1, j):
            visited = visit(i + 1, j)
            q.put(Node(depth + 1, i + 1, j))
    if j < m_index:
        if check(i, j + 1):
            visited = visit(i, j + 1)
            q.put(Node(depth + 1, i, j + 1))
    if i > 0:
        if check(i - 1, j):
            visited = visit(i - 1, j)
            q.put(Node(depth + 1, i - 1, j))
    if j > 0:
        if check(i, j - 1):
            visited = visit(i, j - 1)
            q.put(Node(depth + 1, i, j - 1))
    if visited[n_index][m_index] == 1:
        print(depth + 1)
        return 1

