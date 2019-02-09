def boundary(i,j):
    return i>=0 and i<=(N-1) and j>=0 and j<=(N-1)

def where2d(data,string): #원하는 string이 어디있는지 이차배열에서 찾아주는 함수 만듦 (i,j)형태의 리스트 반환
    row=0;   
    result=[]
    for d in data:
        result+=[(row,i) for i, e in enumerate(d) if e == string]
        row+=1
    return result
    
N=int(input())
village=[]
for i in range(N):
    village+=[' '.join(input()).split()] #하기 전에 '12345'되는 걸 '1','2','3','4','5'로 바꾸는 작업 string은 immutable해서 그랬음..
    #지금 생각해보니 그냥 village+=[list(input())] 해도 되는듯..
    
direction=[[1,0],[0,1],[-1,0],[0,-1]] #driection
def DFS(i,j): #DFS를 썼습니다
    global cnt 
    village[i][j]='0' #방문해서 0으로 바꿔줌 
    for d in direction: # 4방향
        if boundary(i+d[0],j+d[1]): #boundary안에 있으면 실행
            if village[i+d[0]][j+d[1]]=='1': # 간 곳이 1이면 
                village[i+d[0]][j+d[1]]='0' #0으로 바로 바꿔주고
                cnt+=1 # cnt를 1 올려줌 
                DFS(i+d[0],j+d[1]) #재귀함수 써서 이동한 곳에서 또 탐색할 것임
bunji=[]
while where2d(village,'1'): # 1이 있는 동안
    if where2d(village,'1'): #1이 있으면 
        cnt=1 #count 초기화 (4) 초기화됨
        DFS(where2d(village,'1')[0][0],where2d(village,'1')[0][1]) #(1) 1이있는 첫번째 (i,j)를 넣어줌 (5) 1이 있는 첫번째 (i,j)를 넣어줌 
        # village를 아예 0으로 바꿔버려서 두번째가 되어버림
        # (2) 그러면 첫번째 (i,j) 값이 들어가서 끝까지 감 시작한 값에서 더이상 갈 데 없을 때 까지 감~~~으악~~~!~!~ (6) 똑같이 으악!@!~~!
    bunji+=[cnt] # (3) bunji list에 넣어줌 cnt를  (7) bunji list에 넣어줌
    # 더이상 1이 없을 때까지 반복함
print(len(bunji))
for i in sorted(bunji):
    print(i)
