N = int(input())
Podo = [0]
DP = [0]*(N+1)
for i in range(N):
    Podo.append(int(input()))

DP[0] = 0
DP[1] = Podo[1]
if N > 1:
    DP[2] = DP[1] + Podo[2]

for i in range(3, N+1, 1):
    DP[i] = max(DP[i-1], DP[i-2] + Podo[i], DP[i-3] + Podo[i], DP[i-3] + Podo[i-1] + Podo[i])
print(DP[N])