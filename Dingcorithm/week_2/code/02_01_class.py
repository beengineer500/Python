# 생성자 : 객체를 만들 때 호출되는 함수
# 메소드 : 클래스 내부의 함수
# 클래스를 활용해서, 객체가 각자 자기정보에 맞게 행동할 수 있게 만들 수 있다.

class Person:
    def __init__(self, name_pram):  # self : 객체 자기자신을 의미한다.
        self.name = name_pram
        print("Hi I am created", self, self.name)

    def talk(self):
        print("안녕하세요. 저는", self.name, "입니다.")



person1 = Person("유재석")
person1.talk()  # self : 자기 자신에 대한 정보를 가져오기 정보일 뿐, 호출 시 파라미터로 넘겨주지 않아도 된다.

person2 = Person("박명수")
person2.talk()

