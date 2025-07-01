def solution(nums):
    answer = 0
    
    max_nums = len(nums)/2
    
    nums_dict = dict()
    
    for num in nums:
        if (num in nums_dict.keys()):
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    
    max_dict = len(nums_dict.keys())
    
    if (max_nums <= max_dict):
        answer = max_nums
    else:
        answer = max_dict
    
    return answer