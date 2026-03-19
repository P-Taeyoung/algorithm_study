class Dict:
    def __init__(self, length):
        self.items = [None] * length

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, value):
        index = hash(value) % len(self.items)
        return self.items[index]

my_dict = Dict(8)
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!



# 여기서 문제 발생!!  만약 해시된 값 % 배열의 길이를 하여 나온 인덱스 값이 중복될 수 있음.
# 넣어야 할 원소는 a ~ z 총 26개인데 배열길이가 8밖에 안된다면 중복되어 값이 덮이는 수 밖에 없음
# 이를 해결하기 위한 방법으로 연결리스트를 활용할 수 있음. -> 연결지어서 해결한다고 해서 "체이닝(Chaining)"
# Ex) [None, None, (fast, "빠른") → (slow, "느린"), ... ]


class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self, length):
        self.items = []
        for i in range(length):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        # index 번째의 LinkedTuple [(key, value)]
        # 한 번더 호출되는 경우 -> LinkedTuple [(key, value), (key2, value2)]
        return

    def get(self, key):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

my_LinkedDict = LinkedDict(8)
my_LinkedDict.put("77", 4)
my_LinkedDict.put("333", 5)
print(my_LinkedDict.get("77"))

