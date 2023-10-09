def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)

    for patient in emergency:
        rank = sorted_emergency.index(patient) + 1
        answer.append(rank)

    return answer