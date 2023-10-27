def solution(participant, completion):
    participant_dict = {}
    for person in participant:
        participant_dict[person] = participant_dict.get(person, 0) +1
    for person in completion:
        participant_dict[person] -= 1
    
    for person, count in participant_dict.items():
        if count > 0:
            return person