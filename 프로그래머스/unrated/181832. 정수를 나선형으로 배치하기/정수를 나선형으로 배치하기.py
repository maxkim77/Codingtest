def solution(n):
    arr = [[0] * n for _ in range(n)]  # n x n 크기의 2차원 배열을 생성합니다. 초기값은 모두 0입니다.
    num = 1  # 배열에 채워 넣을 숫자입니다.
    x, y = 0, 0  # 현재 위치입니다.
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 오른쪽, 아래, 왼쪽, 위로 이동하는 방향입니다.
    dir_idx = 0  # 현재 방향의 인덱스입니다.
    arr = [[0] * n for _ in range(n)]
    while num <= n * n:  # 1부터 n^2까지 숫자를 채워 넣습니다.
        # 현재 위치에 숫자를 채워 넣습니다.
        arr[x][y] = num
        num += 1

        # 다음 위치를 계산합니다.
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]

        # 다음 위치가 배열의 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향을 시계방향으로 90도 회전합니다.
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny]:
            dir_idx = (dir_idx + 1) % 4
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]

        # 다음 위치로 이동합니다.
        x, y = nx, ny

    return arr
