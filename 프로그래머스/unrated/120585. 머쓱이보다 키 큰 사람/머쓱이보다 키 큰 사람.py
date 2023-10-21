def solution(array, height):
    taller_people = [h for h in array if h > height]
    return len(taller_people)