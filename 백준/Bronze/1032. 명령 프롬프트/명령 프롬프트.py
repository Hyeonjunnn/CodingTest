import sys

n = int(sys.stdin.readline())
tmp = str(sys.stdin.readline().rstrip())

for i in range(n-1):
    tmp2 = []
    inp = str(sys.stdin.readline().rstrip())
    if tmp == inp:
        continue
    else:
        for j in range(len(inp)):
            if inp[j] == tmp[j]:
                tmp2.append(inp[j])
            else:
                tmp2.append('?')
    tmp = ''.join(tmp2)

print(tmp)