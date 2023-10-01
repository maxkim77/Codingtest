def solution(rank, attendance):
    
    available_students = [i for i, is_available in enumerate(attendance) if is_available]
    sorted_students = sorted(available_students, key = lambda x: rank[x])
    a, b, c = sorted_students[0], sorted_students[1], sorted_students[2]
    return 10000 * a + 100 * b + c