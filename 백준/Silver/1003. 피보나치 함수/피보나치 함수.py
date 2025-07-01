case=int(input())
k=0
total0=[]
total1=[]
while k<case:
    i=int(input())
    j=0
    num0=[]
    num1=[]
    if i==0:
        num0=[0,1]
        num1=[0,0]
    else:
        while j<=i:
            if j==0:
                num0.append(1)
                num1.append(0)
                j+=1
            elif j==1:
                num0.append(0)
                num1.append(1)
                j+=1
            else:
                nu0=num0.pop(0)+num0[0]
                nu1=num1.pop(0)+num1[0]
                num0.append(nu0)
                num1.append(nu1)
                j+=1
    total0.append(num0[1])
    total1.append(num1[1])
    k+=1

k=0
while k<case:
    print(str(total0[k])+" "+str(total1[k]))
    k+=1