from datetime import datetime
def solution(a, b):
    date = datetime.strptime(f"2016-{a}-{b}", '%Y-%m-%d')
    return date.strftime("%a").upper()