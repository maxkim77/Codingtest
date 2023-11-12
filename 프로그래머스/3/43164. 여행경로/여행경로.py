def solution(tickets):
    def dfs(city, path):
        nonlocal answer

        # 모든 항공권을 사용한 경우, 현재 경로가 더 우선순위 있는 경로인지 확인
        if len(path) == len(tickets) + 1:
            if not answer:
                answer = path[:]
            return

        # 가능한 다음 도시들을 탐색
        for i, (from_city, to_city) in enumerate(tickets):
            if from_city == city and not used[i]:
                used[i] = True  # 티켓 사용 표시
                dfs(to_city, path + [to_city])
                used[i] = False  # 티켓 사용 해제

    answer = []
    tickets.sort()  # 알파벳 순으로 정렬
    used = [False] * len(tickets)  # 티켓 사용 여부를 저장하는 리스트
    dfs("ICN", ["ICN"])

    return answer
