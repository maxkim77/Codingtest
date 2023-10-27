def solution(genres, plays):
    # 각 장르별 총 재생 횟수를 저장하는 딕셔너리를 생성합니다.
    genre_play_dict = {}
    # 각 장르별 노래 정보를 저장하는 딕셔너리를 생성합니다.
    genre_index_dict = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        # 각 장르별 총 재생 횟수를 계산합니다.
        genre_play_dict[genre] = genre_play_dict.get(genre, 0) + play
        # 각 장르별 노래 정보를 저장합니다.
        if genre not in genre_index_dict:
            genre_index_dict[genre] = []
        genre_index_dict[genre].append((i, play))
    
    # 총 재생 횟수가 많은 장르부터 처리하기 위해 정렬합니다.
    sorted_genres = sorted(genre_play_dict.keys(), key=lambda x: genre_play_dict[x], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        # 각 장르 내에서 많이 재생된 노래부터 처리하기 위해 정렬합니다.
        sorted_genre_songs = sorted(genre_index_dict[genre], key=lambda x: x[1], reverse=True)
        # 최대 두 개의 노래만 선택합니다.
        for i, (index, _) in enumerate(sorted_genre_songs):
            if i >= 2:
                break
            answer.append(index)
    
    return answer