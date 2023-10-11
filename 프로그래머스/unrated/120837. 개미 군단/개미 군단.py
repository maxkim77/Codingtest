def solution(hp):
    general = hp // 5
    remain_hp = hp % 5
    
    soldier = remain_hp // 3
    remain_hp %= 3
    
    worker = remain_hp
    
    return general + soldier + worker