def solution(clothes):
    
    clothes_dict = dict()
    
    for cloth, kind in clothes:
        if (kind in clothes_dict):
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    answer = 1
    for key in clothes_dict:
        answer *= (clothes_dict[key] + 1)
    
    answer -= 1
    
    return answer