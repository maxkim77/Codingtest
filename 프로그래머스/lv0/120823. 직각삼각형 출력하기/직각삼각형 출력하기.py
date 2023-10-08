def triangle(n):
    result = []
    for i in range(1, n+1):
        result.append('*' * i)
    return '\n'.join(result)

n = int(input())
print(triangle(n))