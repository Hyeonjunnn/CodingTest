def solution(participant, completion):
    answer = ''
    
    participant_dict = dict()
    for name in participant:
        if (name not in participant_dict):
            participant_dict[name] = 1
        else:
            participant_dict[name] += 1
    
    completion_dict = dict()
    for name in completion:
        if (name not in completion_dict):
            completion_dict[name] = 1
        else:
            completion_dict[name] += 1
            
    for key, value in participant_dict.items():
        if (key not in completion_dict.keys()):
            answer = key
        elif (value != completion_dict[key]):
            answer = key
    
    return answer