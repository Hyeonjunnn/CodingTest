import sys
import copy

n, m = map(int, sys.stdin.readline().split())

chess_table = [] * n
for i in range(n):
    tmp = list(map(str, sys.stdin.readline()))
    tmp = tmp[:-1]

    chess_table.append(tmp)

copy1_chess_table = copy.deepcopy(chess_table)  # first = 'W'
copy2_chess_table = copy.deepcopy(chess_table)  # first = 'B'

for i in range(len(copy1_chess_table)):
    for j in copy1_chess_table[i]:
        coordinate = copy1_chess_table[i].index(j)
        if (coordinate + i) % 2 == 0:
            if j == 'W':
                copy1_chess_table[i][coordinate] = int(0)
            else:
                copy1_chess_table[i][coordinate] = int(1)
        else:
            if j == 'B':
                copy1_chess_table[i][coordinate] = int(0)
            else:
                copy1_chess_table[i][coordinate] = int(1)

for i in range(len(copy2_chess_table)):
    for j in copy2_chess_table[i]:
        coordinate = copy2_chess_table[i].index(j)
        if (coordinate + i) % 2 == 0:
            if j == 'B':
                copy2_chess_table[i][coordinate] = int(0)
            else:
                copy2_chess_table[i][coordinate] = int(1)
        else:
            if j == 'W':
                copy2_chess_table[i][coordinate] = int(0)
            else:
                copy2_chess_table[i][coordinate] = int(1)

ans = []
for j in range(n - 7):
    for k in range(m - 7):
        result = 0
        for i in range(8):
            result += sum(copy1_chess_table[j + i][0+k:8+k])
        ans.append(result)

for j in range(n - 7):
    for k in range(m - 7):
        result = 0
        for i in range(8):
            result += sum(copy2_chess_table[j + i][0+k:8+k])
        ans.append(result)

print(min(ans))