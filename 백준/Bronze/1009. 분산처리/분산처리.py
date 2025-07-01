case = int(input())

last = []
for i in range(case):
    square = []
    inp = list(map(int, input().split()))
    num = inp[0] % 10
    square.append(num)
    while True:
        num *= inp[0] % 10
        if num % 10 not in square:
            square.append(num % 10)
        else:
            break

    if square[(inp[1]%len(square))-1] == 0:
        last.append(10)
    else:
        last.append(square[(inp[1]%len(square))-1])

for i in range(len(last)):
    print(last[i])