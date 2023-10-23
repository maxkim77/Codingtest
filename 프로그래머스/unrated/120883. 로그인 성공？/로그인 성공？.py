def solution(id_pw, db):
    user_id, user_pw = id_pw
    
    for db_id, db_pw in db:
        if db_id == user_id and db_pw == user_pw:
            return "login"
        elif db_id == user_id:
            return "wrong pw"
        
    return "fail"