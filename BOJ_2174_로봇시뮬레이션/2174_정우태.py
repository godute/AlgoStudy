class node:
    i = 0
    j = 0
    direc = 0
    def __init__(self, i, j, direc):
        self.i = i
        self.j = j
        self.direc = direc
def is_bound(i, j):
    return i >= 1 and i <= B and j >= 1 and j <= A
def command(num, cmd, iter):    # num : 로봇번호, cmd : 명령어, iter : 반복횟수
    for it in range(iter):
        i = robots[num - 1].i
        j = robots[num - 1].j
        ni = i
        nj = j
        direc = robots[num - 1].direc
        if cmd == "L":
            direc += 1
            direc %= 4
        elif cmd == "R":
            direc -= 1
            if direc == -1:
                direc = 3
        else :
            ni += d[direc][0]
            nj += d[direc][1]
        if not(is_bound(ni, nj)):
            print("Robot %d crashes into the wall"%num)     #범위 벗어나면 죽음
            exit()
        if ((i != ni) or (j != nj)) and Map[ni][nj] is not 0:   # 제자리가 아니고, 다음 좌표에 로봇이 있으면?
            print("Robot %d crashes into robot %d"%(num, Map[ni][nj]))  #다른로봇과 충돌문구 출력후 프로그램종료
            exit()
        Map[i][j] = 0
        Map[ni][nj] = num
        robots[num-1].i = ni
        robots[num-1].j = nj
        robots[num-1].direc = direc     #아무런 충돌도 없다면, 계속 명령을 수행함

A, B = list(map(int,input().split()))   # A : 가로, B : 세로
N, M = list(map(int,input().split()))   # N : 로봇개수, M : 명령개수
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 0 = E, 1 = N, 2 = W, 3 = S
robots = list()
Map = list()
for i in range(B+1):
    Map.append([0] * (A+1))

for n in range(N):
    temp = input().split()
    j = int(temp[0])
    i = int(temp[1])
    direc = temp[2]
    if temp[2] == 'E':
        direc = 0
    elif temp[2] == 'N':
        direc = 1
    elif temp[2] == 'W':
        direc = 2
    else :
        direc = 3
    robots.append(node(i, j, direc))    # robot 정보 담아놓음
    Map[i][j] = n+1

for m in range(M):
    temp = input().split()
    num = int(temp[0])
    cmd = temp[1]
    iter = int(temp[2])
    command(num, cmd, iter)
print("OK")