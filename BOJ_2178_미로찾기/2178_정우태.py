import queue

class Node:
    i = None        #리스트의 행 좌표
    j = None        #리스트의 열 좌표
    depth = None    #도달한 거리
    def __init__(self, i, j, depth):
        self.i = i
        self.j = j
        self.depth = depth

def is_bound(i, j): #i, j가 범위에 들어오는지?
    return i>=0 and i < N and j >= 0 and j < M
def BFS():
    while not(q.empty()):   #큐가 빌때까지
        node = q.get()
        if node.i == N-1 and node.j == M-1: #목적지 도달?
            return node.depth
        for k in direction: #for문 하나로 4방향을 볼 수 있음
            ni = node.i + k[0]  #현재 큐에서 pop한 원소의 다음 행을 결정
            nj = node.j + k[1]
            if is_bound(ni, nj) and Map[ni][nj] == '1' and not(Visited[ni][nj]):
                Visited[ni][nj] = True
                q.put(Node(ni, nj, node.depth +1))
    return None
q = queue.Queue()

Map = list()        #전체 맵
Visited = list()    #방문 여부
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #상하좌우 변수

N, M = list(map(int, input().split()))
for i in range(N):
    temp = input()
    Visited.append([False]*M)
    Map.append(temp)
q.put(Node(0, 0, 1))
print(BFS())