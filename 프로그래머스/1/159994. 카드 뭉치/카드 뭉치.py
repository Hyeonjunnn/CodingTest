from collections import deque

def solution(cards1, cards2, goal):
    dq_cards1 = deque(cards1)
    dq_cards2 = deque(cards2)
    dq_goal = deque(goal)
    
    for word in goal:
        if (len(dq_cards1) > 0 and word == dq_cards1[0]):
            dq_cards1.popleft()
            dq_goal.popleft()
        elif (len(dq_cards2) > 0 and word == dq_cards2[0]):
            dq_cards2.popleft()
            dq_goal.popleft()
    
    if (len(dq_goal) != 0):
        answer = 'No'
    else:
        answer = 'Yes'
        
    return answer