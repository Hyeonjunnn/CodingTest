num=list(map(int,input().split() ))

def add(num):
    result=0
    for i in num:
        result+=i
    return result

print(add(num))