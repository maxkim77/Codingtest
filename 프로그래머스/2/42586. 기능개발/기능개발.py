def solution(progresses, speeds):
    answer = []
    days = 0 # 현재까지 계산된 최대 작업 일수
    count = 0 # 같이 배포될 기능의 수

    for progress, speed in zip(progresses, speeds):
        # 해당 기능을 개발 완료하는 데 필요한 일수
        day = (100 - progress) // speed + ((100 - progress) % speed > 0)
        
        # 이전 기능들보다 더 많은 시간이 필요한 경우
        if days < day:
            if count > 0: # 이전까지의 배포할 기능들을 answer에 추가
                answer.append(count)
                count = 0 # 카운트 초기화
            days = day # 최대 작업 일수 갱신
        
        # 같이 배포될 기능의 수 증가
        count += 1

    # 마지막 기능까지 확인했으나 아직 answer에 추가되지 않은 기능들
    answer.append(count)

    return answer