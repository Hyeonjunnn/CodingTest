def dis(x1,y1,x2,y2,r): #distinction the outside or the inside
    x=x2-x1
    y=y2-y1
    distance=x**2+y**2
    if distance<r**2: #inside
        return 1
    else: #outside
        return 0

t=int(input()) #input case T much
total=[]
a=0
while a<t: #test case T
    c=0
    num=list(map(int,input().split()))  #circle's dimension
    c_x1=int(num[0])
    c_y1=int(num[1])
    c_x2=int(num[2])
    c_y2=int(num[3])
    n=int(input())
    b=0
    while b<n: #input planetary system much
        plan=list(map(int,input().split()))
        p_x=plan[0]
        p_y=plan[1]
        p_r=plan[2]
        if dis(c_x1,c_y1,p_x,p_y,p_r)==dis(c_x2,c_y2,p_x,p_y,p_r):
            c+=0
        else:
            c+=1
        b+=1
    total.append(c) #output append
    a+=1

a=0
while a<t:
    print(str(total[a]))
    a+=1