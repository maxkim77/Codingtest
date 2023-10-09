def solution(n, k):
    # Calculate the total cost for the skewers
    skewer_cost = n * 12000
    
    # Calculate the number of drinks that were not free
    extra_drinks = max(0, k - n // 10)
    
    # Calculate the total cost for the extra drinks
    drink_cost = extra_drinks * 2000
    
    # Return the total cost
    return skewer_cost + drink_cost