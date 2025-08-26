def solution(players, callings):
    rank = {}
    cnt = 0
    for name in players:
        rank[name] = cnt
        cnt += 1
    
    for name in callings:
        idx = rank[name]
        
        rank[players[idx]] -= 1
        rank[players[idx - 1]] += 1
    
        players[idx] = players[idx - 1]
        players[idx - 1] = name
        
    answer = players
    return answer