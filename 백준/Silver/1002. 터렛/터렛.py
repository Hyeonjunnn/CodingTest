case=int(input())
result=[]
num=[]

def distance(num):
    x=num[3]-num[0]
    y=num[4]-num[1]
    return x**2+y**2

def gil(num):
    return (num[2]+num[5])**2

def dis(num):
    if distance(num)==0: #같은 좌표
        if num[2]==num[5]: #r1==r2
            return "-1"
        else: #r1!=r2
            return "0"
    else: #다른 좌표
        if distance(num)>(num[2]**2) and distance(num)>(num[5]**2): #외부원
            if distance(num)<gil(num): #좌표2
                return "2"
            elif distance(num)==gil(num): #좌표1
                return "1"
            else: # 좌표0
                return "0"
        else: #내부원
            if num[2]>num[5]: #r1>r2
                if distance(num)>(num[2]-num[5])**2: #좌표2
                    return "2"
                elif distance(num)==(num[2]-num[5])**2: #좌표1
                    return "1"
                else: #좌표0
                    return "0"
            elif num[5]>num[2]: #r1<r2
                if distance(num)>(num[5]-num[2])**2: #좌표2
                    return "2"
                elif  distance(num)==(num[5]-num[2])**2: #좌표1
                    return "1"
                else: #좌표0
                    return "0"
            else: #r1=r2
                if distance(num)<(num[2]+num[5])**2: #좌표2
                    return "2"
                elif distance(num)==(num[2]+num[5])**2: #좌표1
                    return "1"
                else: #좌표0
                    return "0"
i=0
while i<case:
    num=list(map(int,input().split()))
    val=dis(num)
    result.append(val)
    i+=1

j=0
while j<case:
    print(result[j])
    j+=1