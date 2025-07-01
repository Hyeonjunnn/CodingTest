import sys

n, kim, lim = map(int, sys.stdin.readline().split())

count = 0
if kim > lim:
    while True:
        if kim == lim:
            print(count)
            break
        else:
            if kim %2 == 1:
                kim = kim // 2 +1
            else:
                kim = kim // 2
                
            if lim %2 == 1:
                lim = lim // 2 +1
            else:
                lim = lim // 2
        count += 1
else:
    while True:
        if kim == lim:
            print(count)
            break
        else:
            if kim %2 == 1:
                kim = kim // 2 +1
            else:
                kim = kim // 2

            if lim %2 == 1:
                lim = lim // 2 +1
            else:
                lim = lim // 2
        count += 1