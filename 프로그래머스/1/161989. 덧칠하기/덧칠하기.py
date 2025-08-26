def solution(n, m, section):
    arr = [True] * n
    
    for i in section:
        arr[i - 1] = False
    
    cnt = 0
    idx = 0
    for i in arr:
        if (i == False):
            for j in range(m):
                if (idx + j < len(arr)):
                    arr[idx + j] = True
            cnt += 1
            
        idx += 1
    
    answer = cnt
    return answer