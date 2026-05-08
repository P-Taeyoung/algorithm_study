# 내풀이
# 재생된 시간 만큼 악보를 대입하여 배열을 생성
# ex) ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# => ["CDEFGABCDEFGAB", "ABCDE"]
# m 이 배열의 각 원소에 포함되는지 확인 포함되는 곳이 없으면 일치하는 곡이 없는 거이므로 None 반환
# 포함된다면 그 곡을 들은 것이므로 해당 곡 반환. 다만 이 때 포함되는 곡이 여러 곡일 수 있기 때문에
# 가장 길이가 긴 곡을 반환해야 함. 따라서 끝까지 반복은 해야 할 것
# 1번째 오답 포인트
# "#"을 주의해야 함! A#은 하나의 음임.
# 2번째 오답 포인트
# 재생시간만큼 반복해서 재생악보를 만들 때 #을 따로 한음으로 치다보니 정확하게 재생시간만큼의 악보를 만들지 못함.
#
def calculate_time(time1, time2):
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))

    total_m1 = h1 * 60 + m1
    total_m2 = h2 * 60 + m2

    diff = total_m2 - total_m1

    return diff

def convert_to_list(msg):
    list = []
    for s in msg:
        if s == "#":
            list[-1] += "#"
        else:
            list.append(s)
    return list

def solution(m, musicinfos):
    m_sheet = convert_to_list(m)

    max_play_time = -1
    answer = "(None)"

    for i, info in enumerate(musicinfos):
        start, end, title, sheet = info.split(",")

        # 2. 재생 시간 계산 및 악보 리스트화
        play_time = calculate_time(start, end)
        origin_sheet_list = convert_to_list(sheet)

        # 3. 실제 재생된 전체 악보 생성 (함정 해결!)
        # 리스트 곱셈과 슬라이싱을 사용하여 재생 시간만큼만 정확히 생성
        full_sheet_list = (origin_sheet_list * (play_time // len(origin_sheet_list) + 1))[:play_time]

        is_same_song = False
        m_len = len(m_sheet)
        for j in range(len(full_sheet_list) - m_len + 1):
            if full_sheet_list[j : j + m_len] == m_sheet:
                is_same_song = True
                break

        if is_same_song:
            if play_time > max_play_time:
                max_play_time = play_time
                answer = title

    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
