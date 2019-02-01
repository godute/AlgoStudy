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

def where(data,string):
    return [i for i, e in enumerate(data) if e == string]

def reshape(data,n,m):
    new=[]
    for i in range(m):
        small=data[i*m:(i+1)*m]
        new.append(small)
    return new

def countzero(data):
    count=0
    for i in data:
         count+=i.count("0")
    return count

n,m=map(int,input().split())
flat=[]
for i in range(n):
    flat+=input().split()
s=flat

ss=where(s,'0')
i_indicies=[]
j_indicies=[]
i_indicies+=[i//m for i in ss]
j_indicies+=[i%m for i in ss]
s=flat
ss=where(s,'1')
i1_indicies=[]
j1_indicies=[]
i1_indicies+=[i//m for i in ss]
j1_indicies+=[i%m for i in ss]
s=flat
ss=where(s,'2')
i2_indicies=[]
j2_indicies=[]
i2_indicies+=[i//m for i in ss]
j2_indicies+=[i%m for i in ss]
possible_walls=list(itertools.combinations(zip(i_indicies,j_indicies),3))
len(possible_walls)
sumlist=[]
max_val=0
for i in possible_walls:
    visit=copy.copy(reshape(flat,n,m))
    q=collections.deque()
    for j in range(len(i2_indicies)):
        q.append([0,i2_indicies[j],j2_indicies[j]])
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
