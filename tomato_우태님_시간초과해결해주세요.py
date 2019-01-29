import queue
from copy import deepcopy


def cavap(i, j):
    if visit[i][j] == '0':
        visit[i][j] = '1'
        q.put(Node(depth + 1, i, j))


def zero(box):
    for i in box:
        if '0' in i:
            return 0
    return 1



class Node:
    depth = 0

    def __init__(self, depth, i, j):
        self.depth = depth
        self.i = i
        self.j = j


def findone(box):
    i_index = 0
    i_indicies = []
    j_indicies = []
    for i in box:
        i_index += 1
        j_index = 0
        for j in i:
            j_index += 1
            if j == '1':
                i_indicies += [i_index - 1]
                j_indicies += [j_index - 1]
    return i_indicies, j_indicies


# main BFS

m, n = map(int, input().split())
n_index = n - 1
m_index = m - 1

box = []
for i in range(n):
    box.append(input().split())
visit = deepcopy(box)

i_indicies, j_indicies = findone(box)

q = queue.Queue()
for k in range(len(i_indicies)):
    q.put(Node(0, i_indicies[k], j_indicies[k]))
depth = 0
if zero(visit):
    print(depth)
else:
    while (not q.empty()):
        item = q.get()
        i = item.i
        j = item.j
        depth = item.depth
        if i < n_index:
            cavap(i + 1, j)
        if j < m_index:
            cavap(i, j + 1)
        if i > 0:
            cavap(i - 1, j)
        if j > 0:
            cavap(i, j - 1)
        depth = item.depth
    if zero(visit):
        print(depth)
    else:
        print(-1)
