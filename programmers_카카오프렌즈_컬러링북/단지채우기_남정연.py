def boundary(i,j):
    return i>=0 and i<=(N-1) and j>=0 and j<=(N-1)

def where2d(data,string):
    row=0;   
    result=[]
    for d in data:
        result+=[(row,i) for i, e in enumerate(d) if e == string]
        row+=1
    return result
    
N=int(input())
village=[]
for i in range(N):
    village+=[' '.join(input()).split()]
    
direction=[[1,0],[0,1],[-1,0],[0,-1]]
def DFS(i,j):
    global cnt
    village[i][j]='0'
    for d in direction:
        if boundary(i+d[0],j+d[1]):
            if village[i+d[0]][j+d[1]]=='1':
                village[i+d[0]][j+d[1]]='0'
                cnt+=1
                DFS(i+d[0],j+d[1])
bunji=[]
while where2d(village,'1'):
    if where2d(village,'1'):
        cnt=1
        DFS(where2d(village,'1')[0][0],where2d(village,'1')[0][1])
    bunji+=[cnt]
print(len(bunji))
for i in sorted(bunji):
    print(i)
