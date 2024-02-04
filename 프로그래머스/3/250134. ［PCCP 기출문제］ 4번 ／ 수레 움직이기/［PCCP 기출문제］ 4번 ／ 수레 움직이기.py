DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def solution(maze):
    n, m = len(maze), len(maze[0])
    red, blue, target_red, target_blue = find_positions(maze)

    global_minimum = [10**20]  # 리스트로 감싸 global 변수처럼 활용

    def brute_force(red, blue, turn, red_visited, blue_visited):
        nonlocal global_minimum

        # global_minimum을 업데이트 하는 조건!!
        if red == target_red and blue == target_blue:
            global_minimum[0] = min(global_minimum[0], turn)
            return

        red_candidates = cal_cand(red, maze, red_visited, target_red)
        blue_candidates = cal_cand(blue, maze, blue_visited, target_blue)

        for rc in red_candidates:
            for bc in blue_candidates:
                # 도달한 곳이 같으면 안된다, 자리 바꿔치기를 하면 안된다
                if rc != bc and (rc, bc) != (blue, red):
                    new_red_visited = red_visited | {rc}  # 집합 연산을 이용하여 visited 관리
                    new_blue_visited = blue_visited | {bc}

                    brute_force(rc, bc, turn + 1, new_red_visited, new_blue_visited)

    red_visited, blue_visited = {red}, {blue}

    brute_force(red, blue, 0, red_visited, blue_visited)

    return global_minimum[0] if global_minimum[0] != 10**20 else 0

def find_positions(maze):
    n, m = len(maze), len(maze[0])
    for row in range(n):
        for col in range(m):
            if maze[row][col] == 1:
                red = (row, col)
            elif maze[row][col] == 2:
                blue = (row, col)
            elif maze[row][col] == 3:
                target_red = (row, col)
            elif maze[row][col] == 4:
                target_blue = (row, col)

    return red, blue, target_red, target_blue

# cur:본인위치, maze:미로, visited: 본인 visited, target:최종 목적지
def cal_cand(cur, maze, visited, target):
    x, y = cur
    answer = []

    # 이미 도착했으면 도착한 곳을 리턴
    if cur == target:
        return [target]

    # 조건 1. 칸을 벗어나지 않는다
    # 조건 2. visited 딕셔너리에 가려는 칸이 없다
    # 조건 3. 벽이 아니다
    for dx, dy in DIR:
        if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and (x + dx, y + dy) not in visited and \
                maze[x + dx][y + dy] != 5:
            answer.append((x + dx, y + dy))

    return answer
