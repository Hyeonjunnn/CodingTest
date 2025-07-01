def solution(phone_book):
    phone_dict = {} 
    for phone in phone_book: 
        phone_dict[phone] = 1 
    
    for phone in phone_book: 
        arr = "" 
        for num in phone: 
            arr += num
    
            if arr in phone_dict and arr != phone:       
                return False 
                
    return True