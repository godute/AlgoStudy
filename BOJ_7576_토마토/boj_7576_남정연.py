import collections
import copy

def go(i,j):
    if visit[i][j]=='0':
        visit[i][j]='1'
        q.append([depth+1,i,j])
        
def boundary(i,j):
    return i>=0 and j>=0 and i<=n-1 and j<=m-1

def countzero(box):
    count=0
    for i in box:
        count+=i.count('0')
    return count
        
def zero(box):
    for i in box:
        if '0' in i:
            return 0
    return 1

# main BFS
m,n=map(int,input().split())
i_indicies=[]
j_indicies=[]
box=[]
count=-1
for i in range(n):
    tom=input().split()
    box.append(tom)
    for i in tom:
        count+=1
        if i=='1':
            i_indicies+=[count//m]
            j_indicies+=[count%m]
            
visit=copy.copy(box)
q=collections.deque()
for i in range(len(i_indicies)):
    q.append([0,i_indicies[i],j_indicies[i]])
direction=[[1,0],[-1,0],[0,1],[0,-1]]
depth=0
if countzero(visit)==0:
    print(depth)
else:
    while (len(q)):
        item=q.popleft()
        depth=item[0]
        i=item[1]
        j=item[2]
        for d in direction:
            if boundary(i+d[0],j+d[1]):
                go(i+d[0],j+d[1])
    if zero(visit):
        print(depth)
    else:
        print(-1)
