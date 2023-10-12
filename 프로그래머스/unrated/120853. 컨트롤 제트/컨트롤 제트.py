def solution(s):
    elements = s.split()
    stack = []
    total = 0
    for el in elements:
        if el != "Z":
            num = int(el)
            total += num
            stack.append(num)
        else:
            last_added = stack.pop()
            total -= last_added
    return total