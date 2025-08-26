def solution(s):
    answer = 0
    std = ''
    cnt_std = 0
    cnt_else = 0
    for i in s:
        if (std == ''):
            std = i
            cnt_std += 1
        else:
            if (i == std):
                cnt_std += 1
            else:
                cnt_else += 1
                if (cnt_std == cnt_else):
                    answer += 1
                    std = ''
        
    if (std != ''):
        answer += 1
        
    return answer