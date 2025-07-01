import sys

n, m = map(int, sys.stdin.readline().split())
if n >= m:
    std = m
else:
    std = n

square = []
for i in range(n):
    square.append(list(str(sys.stdin.readline().rstrip())))

ans = [1]
while std != 1:
    for i in range(len(square)):
        for j in range(len(square[i])):
            if i + std <= len(square) and j + std <= len(square[i]):
                if square[i][j] == square[i][j + std-1] and square[i][j] == square[i + std-1][j] and square [i][j] == square[i + std-1][j + std-1]:
                    ans.append(std **2)
                else:
                    pass
    else:
        std -= 1

print(max(ans))