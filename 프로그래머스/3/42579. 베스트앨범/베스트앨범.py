def solution(genres, plays):
    
    plays_dict = dict()
    idx_dict = dict()
    
    idx = 0
    for genre in genres:
        if (genre in plays_dict):
            plays_dict[genre] += plays[idx]
        else:
            plays_dict[genre] = plays[idx]
            idx_dict[genre] = dict()
            
        idx_dict[genre][idx] = plays[idx]
        idx += 1
    
    ordered_plays_dict = sorted(plays_dict.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
        
    for key in ordered_plays_dict:
        tmp_list = sorted(idx_dict.get(key[0]).items(), key=lambda x: x[1], reverse=True)
        answer.append(tmp_list[0][0])
        if (len(tmp_list) > 1):
            answer.append(tmp_list[1][0])
    
    return answer