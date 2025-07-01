n = int(input())
a,b,c,d,e,f = map(int, input().split())
num = [a,b,c,d,e,f]
num_copy = [a,b,c,d,e,f]

one_min = min(num)

two = [a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,f+e] # 6C2 = 15
two_min = min(two)

three = [a+b+d,a+b+c,a+d+e,a+e+c,b+d+f,b+c+f,c+e+f,d+e+f]   # 6C3 - (3*4) = 8
three_min = min(three)

if n == 1:
    num_copy.pop(num_copy.index(max(num_copy)))
    print(sum(num_copy))
else:
    side3 = int(4)*three_min
    side2 = int(4*(2*n-3))*two_min
    side1 = int(5*(n**2)-16*n+12)*one_min
    ans = side3+side2+side1
    print(ans)