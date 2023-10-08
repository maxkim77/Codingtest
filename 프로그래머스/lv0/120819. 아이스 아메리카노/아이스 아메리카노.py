def solution(money):
    coffee_price = 5500
    cups = money // coffee_price
    remaining_money = money % coffee_price
    return [cups, remaining_money]