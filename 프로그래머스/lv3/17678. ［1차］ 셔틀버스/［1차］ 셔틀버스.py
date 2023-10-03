def solution(n, t, m, timetable):
    # 분 단위로 변환하는 함수
    def time_to_minutes(time):
        return int(time.split(':')[0]) * 60 + int(time.split(':')[1])

    # 분 단위를 시간으로 변환하는 함수
    def minutes_to_time(minutes):
        return '{:02d}:{:02d}'.format(minutes // 60, minutes % 60)

    crew_arrival_times = sorted([time_to_minutes(time) for time in timetable])

    last_bus_time = 540 + (n - 1) * t  # 09:00은 540분

    for i in range(n):
        if i == n - 1:  # 마지막 버스
            if len(crew_arrival_times) < m:  # 마지막 버스에도 자리가 남아 있을 때
                return minutes_to_time(last_bus_time)
            elif crew_arrival_times[m - 1] <= last_bus_time:  # 마지막 버스에 타려면 m번째 크루보다 1분 일찍 와야 함
                return minutes_to_time(crew_arrival_times[m - 1] - 1)
            else:  # 마지막 버스에도 탈 수 없는 경우
                return minutes_to_time(last_bus_time)
        # 버스에 탈 크루들 제거
        for j in range(m - 1, -1, -1):
            if len(crew_arrival_times) == 0:
                break
            if crew_arrival_times[0] <= 540 + i * t:  # 크루의 도착 시간이 버스 도착 시간보다 이른 경우
                crew_arrival_times.pop(0)
