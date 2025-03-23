# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
#
# 노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.
#
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
#
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
#
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
#
#
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
#
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.

# # 1
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# # 정답 = [4, 1, 3, 0]
#
#
# # 2
# genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
# plays = [2000, 500, 600, 150, 800, 2500, 2000]
# # 정답 = [0, 6, 5, 2, 4, 1]

# def get_melon_best_album(genre_array, play_array):
#     playlist = {}
#     for index, (genre, play) in enumerate(zip(genre_array, play_array)):
#         if genre in playlist:
#             playlist[genre].append([index, play])
#         else:
#             playlist[genre] = [[index, play]]
#
#
#     # 구현해보세요!
#     return []


# 못풀겠다...



def get_melon_best_album(genre_array, play_array):
    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.(단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
    # "가장 많이" => 정렬! : 특정 키값이 특정되지 않았지만 밸류를 합치고 싶다 : 딕셔너리!
    # n = len(genre_array)
    # genre_total_play_dict = {}
    # for i in range(n):
    #     genre = genre_array[i]
    #     play = play_array[i]
    #     if genre not in genre_total_play_dict:
    #         genre_total_play_dict[genre] = play
    #     else:
    #         genre_total_play_dict[genre] += play
    #
    # print(genre_total_play_dict)

    # 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
    # 다시 배열 탐색해야하나? 다시 딕셔너리를 만들어보자 => 키: (인덱스, 재생횟수)[]
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_total_play_dict)
    # {'classic': 1450, 'pop': 3100} 이 출력됩니다!
    print(genre_index_play_array_dict)
    # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]} 이 출력됩니다!

    # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
    # value(재생수)를 기준으로 정렬하자

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_array)

    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result

# ☝ 여기서 sorted 함수는 reverse=True`로 재생 횟수를 기준으로 내림차순 정렬하고 있습니다.
#
# 하지만 재생 횟수가 동일한 경우에는, Python의 sorted 함수는 **안정 정렬(stable sort)**을 사용하기 때문에, 원래 입력 순서(즉, 인덱스 순서)를 유지합니다.
#
# 즉, genre_index_play_array_dict[genre] 리스트는 처음에 인덱스 순서대로 저장되었으므로, 동일한 재생 횟수를 가진 노래는 자연스럽게**인덱스가 낮은 순서대로**정렬됩니다.

# def get_melon_best_album(genre_array, play_array):
#     # 1. dict 에 장르별로 얼마나 재생횟수를 가지고 있는가
#     # 2. dict 에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가
#
#     n = len(genre_array)
#     genre_total_play_dict = {}
#     genre_index_play_array_dict = {}
#
#     for i in range(n):
#         genre = genre_array[i] # classic
#         play = play_array[i] # 500
#
#         if genre in genre_total_play_dict: #classic 이라는 키값이 있었으면
#             genre_total_play_dict[genre] += play #재생횟수를 더해줘야 할테니까요
#             genre_index_play_array_dict[genre].append([i, play])
#         else: #키 값이 없는 상황이라면
#             genre_total_play_dict[genre] = play # 500
#             genre_index_play_array_dict[genre] = [[i, play]]
#
#     # 장르별로 가장 재생횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력하기.
#     sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
#
#     result = []
#     for genre, total_play in sorted_genre_play_array:
#         sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)
#
#         genre_song_count = 0
#         for index, play in sorted_genre_index_play_array:
#             if genre_song_count >= 2:
#                 break
#
#             result.append(index)
#             genre_song_count += 1

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))