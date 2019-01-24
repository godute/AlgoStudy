## queue

def move(Q,d,m):
    if d==(-1): #앞으로 한 칸씩 땡기는거
        QQ=['NaN']*(m-1)
        for i in range(1,m):
            QQ[i-1]=Q[i]
    elif d==1: #뒤로 한 칸씩 미는거
        QQ=['NaN']*(m+1)
        for j in range(m):
            QQ[j+1]=Q[j]
    return QQ
    
n=int(input())
Q=[]
for i in range(n):
    command=input()
    command0=command.split()[0]
    if len(command.split())==2:
        command1=int(command.split()[1])
    if command0=="push":
        Q+=[command1]
    if command0=="pop":
        if not Q:print("-1")
        else:print(Q[0])
        Q=move(Q,-1,len(Q))
    if command0=="size":
        print(len(Q))
    if command0=="empty":
        if Q:print("0")
        else: print("1")
    if command0=="front":
        if not Q: print("-1")
        else: print(Q[0])
    if command0=="back":
        if not Q: print("-1")
        else: print(Q[len(Q)-1])

## stack 

n=int(input())
Q=[]
for i in range(n):
    command=input()
    command0=command.split()[0]
    if len(command.split())==2:
        command1=int(command.split()[1])
    if command0=="push":
        Q=move(Q,1,len(Q))
        Q[0]=command1
    if command0=="pop":
        if not Q:print("-1")
        else:print(Q[0])
        Q=move(Q,-1,len(Q))
    if command0=="size":
        print(len(Q))
    if command0=="empty":
        if Q:print("0")
        else: print("1")
    if command0=="top":
        if not Q: print("-1")
        else: print(Q[0])
        
  ## 원형 큐 ?
  def move(Q,d,m):
    if d==(-1): #앞으로 한 칸씩 땡기는거
        QQ=['NaN']*m
        for i in range(m):
            QQ[i-1]=Q[i]
    elif d==1: #뒤로 한 칸씩 미는거
        QQ=['NaN']*m
        for j in range(m):
            QQ[(j+1)%m]=Q[j]
    return QQ
    
    n=int(input())
Q=[]
for i in range(n):
    command=input()
    command0=command.split()[0]
    if len(command.split())==2:
        command1=int(command.split()[1])
    if command0=="push":
        Q+=[command1]
    if command0=="pop":
        if Q[0]=='NaN':print("-1")
        else:
            print(Q[0])
            Q[0]='NaN'
            Q=move(Q,-1,len(Q))
    if command0=="size":
        print(len(Q))
    if command0=="empty":
        if Q:print("0")
        else: print("1")
    if command0=="front":
        if Q[0]=='NaN: print("-1")
        else: print(Q[0])
    if command0=="back":
        if not Q: print("-1")
        else: print(Q[len(Q)-1])

