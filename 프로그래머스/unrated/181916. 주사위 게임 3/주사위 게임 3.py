def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_count = {i: dice.count(i) for i in set(dice)}

    # 네 주사위에서 나온 숫자가 모두 같은 경우
    if len(dice_count) == 1:
        return 1111 * a

    # 세 주사위에서 나온 숫자가 같은 경우
    elif 3 in dice_count.values():
        p = [key for key, value in dice_count.items() if value == 3][0]
        q = [key for key, value in dice_count.items() if value == 1][0]
        return (10 * p + q) ** 2

    # 주사위가 두 개씩 같은 값이 나오는 경우
    elif len(dice_count) == 2 and 2 in dice_count.values():
        p, q = dice_count.keys()
        return (p + q) * abs(p - q)

    # 어느 두 주사위에서 나온 숫자가 같은 경우
    elif len(dice_count) == 3:
        p = [key for key, value in dice_count.items() if value == 2][0]
        q, r = [key for key, value in dice_count.items() if value == 1]
        return q * r

    # 네 주사위에 적힌 숫자가 모두 다른 경우
    else:
        return min(dice)