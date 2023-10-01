def solution(order):
    total_price = 0
    price_americano = 4500
    price_cafelatte = 5000

    for item in order:
        if item in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            total_price += price_americano
        elif item in ["icecafelatte", "cafelatteice", "cafelatte"]:
            total_price += price_cafelatte
        elif item in ["hotcafelatte", "cafelattehot"]:
            total_price += price_cafelatte

    return total_price