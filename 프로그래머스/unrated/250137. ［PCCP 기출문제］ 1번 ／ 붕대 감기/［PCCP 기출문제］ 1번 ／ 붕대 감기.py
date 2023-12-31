def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    continuous_success = 0
    next_attack_index = 0

    for second in range(1001):
        if next_attack_index < len(attacks) and attacks[next_attack_index][0] == second:
            current_health -= attacks[next_attack_index][1]
            continuous_success = 0
            next_attack_index += 1

            if current_health <= 0:
                return -1

        else:
            # 최대 체력을 초과하지 않는 경우에만 회복 적용
            if current_health < health:
                if continuous_success < t:
                    current_health += x
                    continuous_success += 1

                # 추가 회복량 적용 후 다음 회복까지 기다림
                if continuous_success == t:
                    current_health = min(current_health + y, health)  # 추가 회복도 최대 체력을 초과하지 않도록
                    continuous_success = 0  # 연속 성공 초기화

    return current_health
