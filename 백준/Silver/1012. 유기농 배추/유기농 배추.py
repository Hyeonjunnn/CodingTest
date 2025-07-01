import sys
sys.setrecursionlimit(10**9)

def dfs(lis):
    i,j = map(int, lis)
    adj[i][j] = 0
    while True:
        if 0 <= j <= m-1 and  0 <= i <= n-1:
            if j < m-1 and adj[i][j+1] == 1:    #right
                dfs([i,j+1])
            elif 0 < j and adj[i][j-1] == 1:  #left
                dfs([i,j-1])
            elif i < n-1 and adj[i+1][j] == 1:   #down
                dfs([i+1,j])
            elif 0 < i and adj[i-1][j] == 1: #up
                dfs([i-1,j])
            else: break
        else: break
    return 1

case = int(input())

last = []
for i in range(case):
    adj = []
    m, n, k = map(int, input().split()) #m = row(x), n = column(y), k = cabagge quantity
    for i in range(n):
        adj.append([])
        for j in range(m):
            adj[i].append(0)
    for i in range(k):
        x,y = map(int, input().split())
        adj[y][x] = 1
    count = 0

    for j in range(m):
        for i in range(n):
            if adj[i][j] == 1:
                lis = [i,j]
                count += dfs(lis)
            else: pass
    last.append(count)

for i in range(len(last)):
    print(last[i])