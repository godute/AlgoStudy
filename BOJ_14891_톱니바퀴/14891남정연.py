def move(t,d):
    tt=[90,91,92,93,94,95,96,97]
    if d==(-1):
        for i in range(8):
            tt[i-1]=t[i]
    elif d==1:
         for j in range(8):
            tt[(j+1)%8]=t[j]
    return tt

def l_move(t1,t2,d1): #첫번째 톱니바퀴(인수)가 움직일때
    m=0
    if t1[2]==t2[6]:
        t1=move(t1,d1)
    elif t1[2]!=t2[6]:
        t1=move(t1,d1)
        t2=move(t2,-d1)
        m=1
    return t1,t2,m

def r_move(t1,t2,d2): #두번째 톱니바퀴(인수)가 움직일때
    m=0
    if t1[2]==t2[6]:
        t2=move(t2,d2)
    elif t1[2]!=t2[6]:
        t1=move(t1,-d2)
        t2=move(t2,d2)
        m=1
    return t1,t2,m

def tot_move(t1,t2,t3,t4,a,b):
    tt2=t2.copy()
    tt3=t3.copy()
    if a==1:
        t1,t2,m=l_move(t1,t2,b)
        if m:
            x,t3,m=l_move(tt2,t3,-b)
        if m:
            x,t4,m=l_move(tt3,t4,b)
        return t1,t2,t3,t4
    elif a==2:
        t1,t2,m=r_move(t1,t2,b)
        x,t3,m=l_move(tt2,t3,b)
        if m:
            x,t4,m=l_move(tt3,t4,-b)
        return t1,t2,t3,t4
    elif a==3:
        x,t4,m=l_move(tt3,t4,b)
        t2,t3,m=r_move(t2,t3,b)
        if m:
            t1,x,m=r_move(t1,tt2,-b)
        return t1,t2,t3,t4
    elif a==4:
        t3,t4,m=r_move(t3,t4,b)
        if m:
            t2,t3,m=r_move(t2,tt3,-b)
        if m:
            t1,x,m=r_move(t1,tt2,b)
        return t1,t2,t3,t4

def get_score(t1,t2,t3,t4):
    count=0
    if t1[0]==1:
        count+=1
    if t2[0]==1:
        count+=2
    if t3[0]==1:
        count+=4
    if t4[0]==1:
        count+=8
    return count

# 톱니바퀴


t=input()
t1=[int(i) for i in t]
t=input()
t2=[int(i) for i in t]
t=input()
t3=[int(i) for i in t]
t=input()
t4=[int(i) for i in t]
n=int(input())
score=0
for i in range(n):
    a,b=map(int,input().split())
    t1,t2,t3,t4=tot_move(t1,t2,t3,t4,a,b)

score=get_score(t1,t2,t3,t4)
print(score)
