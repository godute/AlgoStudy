from functools import reduce

def div(a,b): #문제가 정의한 나누기처럼 만들었음
    return a//b if a>0 else -(abs(a)//b)
def setparam(): #파라미터값들이 어떤지 한번에 받아오려고 만듦
    return result_vec[-1][0],result_vec[-1][1],result_vec[-1][2]
def check(a): #연산자 쓸 수 있는 카드가 남았는지 안남았는지 확인+방문한 노드는 아닌지 확인
    return oplist[a] and not(result_vec[-1][1]+[a] in visited_op)
def fill_op(new): #다시 돌아올때 직전의 연산자 개수 충전
    oplist[result_vec[-1][1][-1]]+=1
N=int(input())
numlist=list(map(int,input().split()))
oplist=list(map(int,input().split())) #op몇개씩 있는지 확인
result_vec=[] #[result, operator list, depth]형태로 stack 쌓을거임
output=[] #끝까지 간 노드들만 쌓이는 곳
visited_op=[] #방문한 연산자들의 리스트들이 쌓이는 곳
new=[numlist[0],list(),0] #초기값 넣어줌, 맨첫숫자, 빈 연산자리스트, depth=0임
result_vec+=[new] #stack에 초기node 넣어줌

# 0 : +
# 1 : -
# 2 : *
# 3 : //

while 1:
    if not result_vec: #비어있으면 나가자
        break
    if result_vec[-1][2]==N-1:#끝까지 가면,
        old=result_vec.pop()  #맨마지막 노드 빼내자
        output.append(old)    #그리고 맨마지막 노드만 모아놓은 output리스트에 넣자
        oplist[old[1][-1]]+=1 #다시돌아가니까 연산자 갯수 늘려줌
        visited_op.append(old[1]) #방문한 노드 리스트에 넣어줌
    if check(0): #더하기면,
        num,opp,depth=setparam() #파라미터 셋팅 먼저..
        new=[num+numlist[depth+1],opp+[0],depth+1] #현재 있는 숫자랑 다음숫자랑 더하고,
        # 연산자 리스트에도 넣어주고 depth도 하나 추가함..
        result_vec.append(new) #스택에 쌓아줌
        oplist[0]-=1 #썼으니까 연산자 한개 줄어들음
        continue
    if check(1):#빼기
        num,opp,depth=setparam()
        new=[num-numlist[depth+1],opp+[1],depth+1]
        result_vec.append(new)
        oplist[1]-=1
        continue
    if check(2):#곱하기
        num,opp,depth=setparam()
        new=[num*numlist[depth+1],opp+[2],depth+1]
        result_vec.append(new)
        oplist[2]-=1
        continue
    if check(3) :#나누기
        num,opp,depth=setparam()
        new=[div(num,numlist[depth+1]),opp+[3],depth+1]
        result_vec.append(new)
        oplist[3]-=1
        continue
    else:
        new=result_vec.pop() #넷다 안되면,막힌 길이다
        visited_op.append(new[1]) #막힌길이니까 넣어주자 
        try: #new가 비어있을 때가 있어서 indexerror가 나서 그냥 넘어가는 모습
            oplist[new[1][-1]]+=1 
        except IndexError:
            continue
print(reduce(lambda a,b: a if a > b else b,output)[0]) #lambda, reduce 이용
print(reduce(lambda a,b: a if a < b else b,output)[0])
