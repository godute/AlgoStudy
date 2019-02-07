import itertools
import copy
import collections


def go(i,j):
    if visit[i][j]=='0':
        visit[i][j]='2'
        q.append([depth+1,i,j])
        
def boundary(i,j):
    return i>=0 and j>=0 and i<=n-1 and j<=m-1

def countzero(flat):
    count=0
    for i in flat:
        count+=i.count('0')
    return count
        
def zero(flat):
    for i in flat:
        if '0' in i:
            return 0
    return 1


def where2d(data,string):
    row=0;   
    result=[]
    for d in data:
        result+=[[row,i] for i, e in enumerate(d) if e == string]
        row+=1
    return result


def countzero(data):
    count=0
    for i in data:
         count+=i.count("0")
    return count

n,m=map(int,input().split())
flat=[]
for i in range(n):
    flat+=[input().split()]
    
index_0=where2d(flat,'0')
index_2=where2d(flat,'2')

possible_walls=itertools.combinations(index_0,3)
sumlist=[]
max_val=0

for i in possible_walls:
    visit=copy.deepcopy(flat)
    q=collections.deque()
    for h in range(len(index_2)):
        q.append([0,index_2[h][0],index_2[h][1]])
    direction=[[1,0],[-1,0],[0,1],[0,-1]]
    visit[i[0][0]][i[0][1]]='1'
    visit[i[1][0]][i[1][1]]='1'
    visit[i[2][0]][i[2][1]]='1'
    while (len(q)):
        item=q.popleft()
        depth=item[0]
        i=item[1]
        j=item[2]
        for d in direction:
            if boundary(i+d[0],j+d[1]):
                go(i+d[0],j+d[1])
    mm=countzero(visit)
    if mm>max_val:
        max_val=mm 
print(max_val)
