def solution(wallpaper):
    min_x = len(wallpaper[0]) + 1
    max_x = 0
    min_y = len(wallpaper) + 1
    max_y = 0
    
    tmp_y = 0
    chk = 0
    for i in wallpaper:
        tmp_x = 0
        
        for j in i:
            if (j == '#'):
                chk = 1
                if(min_x > tmp_x):
                    min_x = tmp_x
                if(max_x < tmp_x):
                    max_x = tmp_x
                    
            tmp_x += 1
        if (chk == 1):
            if (min_y > tmp_y):
                min_y = tmp_y
            if (max_y < tmp_y):
                max_y = tmp_y
            chk = 0
        tmp_y += 1
        
    answer = [min_y, min_x, max_y + 1, max_x + 1]
    return answer