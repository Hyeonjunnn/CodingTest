n, l = map(int, input().split())

while True:
    dis = (n/l)-(n//l)
    if l%2 == 1 and dis == 0:   #l is odd num and dis = 0
        standard_num = n//l
        if standard_num-(l//2) < 0:
            l += 1
            continue
        else:
            for i in range(l):
                    print((standard_num-(l//2))+i, end = ' ')
        break
    elif l%2 == 0 and dis == 0.5:   #l is even num and dis = 0.5
        standard_num = n/l
        if int(standard_num-(l//2)+0.5) < 0:
            l +=1
            continue
        else:
            for i in range(l):
                print(int(standard_num-(l//2)+i+0.5), end = ' ')
        break
    elif l == 100 or n < l:
        print(-1)
        break
    l+=1