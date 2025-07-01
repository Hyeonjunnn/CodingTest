def cal(x,y):
    sum = 1
    if x*2 > y:
        x = y-x
    else: pass
    i = x
    while i > 0:
        sum *= ((y-x)/i)+1
        i -= 1
    return round(sum)


case = int(input())

last = []
for i in range(case):
    x,y = map(int, input().split())
    if x == y:
        last.append(1)
    else:
        last.append(cal(x,y))
for i in range(len(last)):
    print(last[i])