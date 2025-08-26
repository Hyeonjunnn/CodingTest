def solution(keymap, targets):
    dic = {}
    for row_key in keymap:
        cnt = 1
        for key in row_key:
            if(key not in dic or dic[key] > cnt):
                dic[key] = cnt
            cnt += 1
        
    answer = []
    for row_target in targets:
        
        sum_key = 0
        for key in row_target:
            if (key not in dic):
                sum_key = -1
                break
            else:
                sum_key += dic[key]
            
        answer.append(sum_key)
    
    return answer