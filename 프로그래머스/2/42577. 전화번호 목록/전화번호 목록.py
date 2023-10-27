def solution(phone_book):
    phone_book.sort() #전화번호 목록을 정렬
    
    for i in range(len(phone_book) - 1):
        # 현재 번호와 다음 전화번호를 비교하여 접두어 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False 
        
    return True