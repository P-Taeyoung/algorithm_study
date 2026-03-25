# Q. 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
# 노래는 인덱스로 구분하며, 노래를 수록하는 기준은 다음과 같다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.

# 내풀이
def get_melon_best_album_1(genre_array, play_array):
    # 구현해보세요!
    arr = []
    #해시를 이용하여 장르별 재생수를 구함.
    genre_hash = {}
    for genre, play in zip(genre_array, play_array):
        genre_hash[genre] = genre_hash.get(genre, 0) + play

    #장르별 재생수를 기준으로 정렬
    genre_hash = sorted(genre_hash.items(), key=lambda x: x[1], reverse=True)


    for genre in genre_hash:
        first_idx = -1 # 가장 많이 들은 재생곡 인덱스
        second_idx = -1 # 두번째
        first_count = 0 #재생수를 비교하기 위함.
        second_count = 0
        for i in range(0, len(play_array)):
            if genre_array[i] == genre[0]: # 현재 재생수가 가장 많은 장르부터 찾아서 수록함.
                if play_array[i] > first_count: # 재생수대로 순위 설정 (앞부터 탐색하기 때문에 자연스럽게 동률일 경우 앞선 인덱스부터 수록됨)
                    second_count = first_count
                    first_count = play_array[i]
                    second_idx = first_idx
                    first_idx = i
                elif play_array[i] > second_count:
                    second_count = play_array[i]
                    second_idx = i

        arr.append(first_idx)
        arr.append(second_idx)
    return arr


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album_1(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album_1(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))