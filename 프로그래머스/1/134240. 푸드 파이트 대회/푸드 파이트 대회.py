def solution(food):
    
    arr_food = food[1:]
    result_arr = []
    answer = ''
    idx = 1
    for num in arr_food:
        result_arr.append(str(idx) * int(num/2))
        answer += str(idx) * int(num/2)
        idx += 1
        
    result_arr.reverse()
    
    answer += '0'
    for i in result_arr:
        answer += i
    
    return answer