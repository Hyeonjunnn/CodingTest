import sys

n = int(input())
relation = []
relation = [[]] * n
for i in range(n):
    relation[i] = list(map(str, sys.stdin.readline().rstrip()))

ans = []
for i in range(n):
    ans.append([0] * n)

for i in range(n):
    for j in range(len(relation[i])):
        if relation[i][j] == 'Y':
            ans[i][j] = 1
            for h in range(len(relation[j])):
                if relation[j][h] == 'Y':
                    ans[i][h] = 1
    ans[i][i] = 0

add = []
for i in ans:
    add.append(sum(i))
    
print(max(add))