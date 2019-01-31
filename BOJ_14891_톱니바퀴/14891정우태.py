#톱니바퀴 회전할지 여부 결정함수, 재귀호출
def sol(index, direction, k_value):  #index : 현재 톱니바퀴, direction : 진행 방향, k_value : 시계?반시계?
    if direction == -1: #왼쪽으로 진행중
        if index == 0: #첫 번째 톱니바퀴면
            return None  #종료
        if Gear[index][6] != Gear[index-1][2]: # 맞닿은 부분이 다르면?
            is_rotation[index-1] = -k_value  #현재 톱의 반대방향으로 왼쪽톱이 회전 가능함
            sol(index - 1, direction, -k_value) #왼쪽 톱도 한번 보자.
    else : #오른쪽으로 진행중
        if index == 3:
            return None
        if Gear[index][2] != Gear[index+1][6]:
            is_rotation[index+1] = -k_value
            sol(index + 1, direction, -k_value)

#회전시켜주는 함수
def rotation(index, k_value): #톱니 인덱스와 회전 방향을 받아서, 해당 톱니 회전시켜보자.
    if k_value == -1:
        temp_r = Gear[index][0]
        for x in range(7):
            Gear[index][x] = Gear[index][x+1]
        Gear[index][7] = temp_r
    elif k_value == 1:
        temp_r = Gear[index][7]
        for x in range(7, 0, -1):
            Gear[index][x] = Gear[index][x-1]
        Gear[index][0] = temp_r
    else:
        return None
def Print_Gear():
    for i in range(4):
        for j in range(8):
            print(Gear[i][j], end='')
        print()

Gear = list()  # 톱니바퀴 값
k_list = list()  # 명령 값
is_rotation = [0, 0, 0, 0]  # 회전 가능한지 저장한 리스트 (1 -> 시계, -1 -> 반시계)


for i in range(4):
    text = input()
    temp = list()
    for j in range(8):
        temp.append(int(text[j]))
    Gear.append(temp)

K = int(input())
for k in range(K):
    temp = list(map(int, input().split()))  # input받고 split, int형 변환 동시에
    k_list.append(temp)

for k in range(K):
    for r in range(4):
        is_rotation[r] = 0
    cur_index = k_list[k][0] - 1
    is_rotation[cur_index] = k_list[k][1]
    sol(cur_index, -1, k_list[k][1])  # 왼쪽 진행
    sol(cur_index, 1, k_list[k][1])  # 오른쪽 진행
    
    for r in range(4):
        rotation(r, is_rotation[r])

#Print_Gear()
Result = 0
for r in range(4):
    if Gear[r][0] == 1:
        Result += 2 ** r

print(Result)