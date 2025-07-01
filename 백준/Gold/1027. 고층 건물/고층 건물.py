n = int(input())
height = list(map(int, input().split()))

ans = []
st_x = 0
for st_y in height:
    left = height[:st_x]
    right = height[st_x+1:]
    left.reverse()
    j = 1
    count = 0
    standard = 999999999999999999999999
    for i in left:
        tem = (st_y-i)/j
        if tem < standard:
            count += 1
            standard = tem
        j += 1
    j = 1
    standard = -99999999999999999999999
    for i in right:
        tem = (i-st_y)/j
        if tem > standard:
            count += 1
            standard = tem
        j += 1
    ans.append(count)
    st_x += 1


print(max(ans))