def solution(myStr):
    separators = ['a', 'b', 'c']
    for sep in separators:
        myStr = myStr.replace(sep,'|')
    result = [s for s in myStr.split('|') if s]
    return result if result else ["EMPTY"]