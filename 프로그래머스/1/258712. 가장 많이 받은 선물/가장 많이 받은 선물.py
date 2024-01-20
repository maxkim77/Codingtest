import numpy as np

def solution(friends, gifts):
    dic = {f:i for i, f in enumerate(friends)} # 인덱스 저장
    table = [ [0] * len(friends) for _ in range(len(friends))] # 선물 준 리스트
    presents = [0] * len(friends)
    
    for gift in gifts:
        g, t = gift.split()
        table[dic[g]][dic[t]] += 1
    
    array = np.array(table)
    
    t_given = array.sum(axis = 1)
    t_taken = array.sum(axis = 0)
    point = list(t_given - t_taken)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)): #이미 순환한 i를 순환하지 않도록 i  + 1
            if table[i][j] > table[j][i]: # i가 준 게 더 많으면
                presents[i] += 1
            elif table[j][i] > table[i][j]: # j가 준 게 더 많으면
                presents[j] += 1
            else: # 같으면
                if point[i] > point[j]:
                    presents[i] += 1
                if point[j] > point[i]:
                    presents[j] += 1

    return max(presents)