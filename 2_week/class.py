class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("I am a person", self, self.name)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다.")


person_1 = Person("james")
print(person_1.name)
person_1.talk()
person_2 = Person("mike")
print(person_2.name)
person_2.talk()
