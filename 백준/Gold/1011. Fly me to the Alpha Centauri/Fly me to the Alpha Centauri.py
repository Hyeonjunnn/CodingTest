def cal(dis):
    sum = 0
    num = 1
    while True:
        if sum + num < dis:
            sum += num*2
            num += 1
        else:
            if sum < dis <= sum + num:
                return (num*2)-1
            else:
                return (num-1)*2

case = int(input())

last = []
for i in range(case):
    x,y = map(int, input().split())
    last.append(cal(y-x))

for i in range(len(last)):
    print(last[i])