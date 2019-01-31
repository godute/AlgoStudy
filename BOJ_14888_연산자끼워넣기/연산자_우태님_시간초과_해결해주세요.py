import copy
from functools import reduce

def div(a,b):
    return a//b if a>0 else -(abs(a)//b)
def setparam():
    return result_vec[-1][0],result_vec[-1][1],result_vec[-1][2]
def check(a):
    return oplist[a] and not(result_vec[-1][1]+[a] in visited_op)
def fill_op(new):
    oplist[result_vec[-1][1][-1]]+=1
N=int(input())
numlist=list(map(int,input().split()))
op=list(map(int,input().split()))
oplist=copy.copy(op) #op몇개남았느니
result_vec=[]
output=[]
visited_op=[]

# [result, operator list, depth]
new=[numlist[0],list(),0]
result_vec+=[new]
depth=0
result_vec

while 1:
    if not result_vec:
        break
    if result_vec[-1][2]==N-1:
        old=result_vec.pop()
        output.append(old)
        oplist[old[1][-1]]+=1
        visited_op.append(old[1])
    if check(0):
        num,opp,depth=setparam()
        new=[num+numlist[depth+1],opp+[0],depth+1]
        result_vec.append(new)
        oplist[0]-=1
        continue
    if check(1):
        num,opp,depth=setparam()
        new=[num-numlist[depth+1],opp+[1],depth+1]
        result_vec.append(new)
        oplist[1]-=1
        continue
    if check(2):
        num,opp,depth=setparam()
        new=[num*numlist[depth+1],opp+[2],depth+1]
        result_vec.append(new)
        oplist[2]-=1
        continue
    if check(3) :
        num,opp,depth=setparam()
        new=[div(num,numlist[depth+1]),opp+[3],depth+1]
        result_vec.append(new)
        oplist[3]-=1
        continue
    else:
        new=result_vec.pop()
        visited_op.append(new[1])
        try:
            oplist[new[1][-1]]+=1
        except IndexError:
            continue

print(reduce(lambda a,b: a if a > b else b,output)[0])
print(reduce(lambda a,b: a if a < b else b,output)[0])
