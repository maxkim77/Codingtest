def solution(order):
    order_str = str(order)
    clap_count = 0
    
    for digit in order_str:
        if digit in '369':
            clap_count += 1
    return clap_count