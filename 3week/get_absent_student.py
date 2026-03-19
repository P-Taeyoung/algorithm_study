# Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 내풀이
# 해시테이블을 이용하여 all_students배열에 있는 이름을 해싱하여 인덱스 값으로 변환 후 해당 이름을 저장
# 추후 present_students 이름을 통해 값이 있는 경우에는 출석으로 인정된 것이고 값이 없다면 출석이 안된 것임.
def get_absent_student_1(all_array, present_array):
    # 구현해보세요!
    length = len(all_array)
    dict = [None] * len(all_array)

    for student in present_array:
        index = hash(student) % length
        dict[index] = student

    for student in all_array:
        index = hash(student) % length
        if dict[index] is None:
            return student
    return "충돌 발생"

# 내풀이_2 if - in 함수를 이용하여 값 반환
def get_absent_student_2(all_array, present_array):

    for student in all_array:
        if student not in present_array:
            return student
    return None


def get_absent_student_3(all_array, present_array):
    dict = {} # dict = {}라고 선언하는 순간 파이썬은 이를 '딕셔너리(해시 테이블)' 객체로 생성
    for key in all_array:
        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key


print("-- 내풀이 1 --")
print(get_absent_student_1(all_students, present_students))
print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student_1(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student_1(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))
# 위에서는 충돌이 일어나는 경우 None 값이 반횐될 것임.
print("-- 내풀이 2 --")
print(get_absent_student_2(all_students, present_students))
print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student_2(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student_2(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))