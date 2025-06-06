## Class (클래스)
- 클래스는 객체를 정의한 설계도 또는 틀입니다.
- 클래스를 이용하면, 같은 속성과 기능을 가진 객체들을 묶어서 정의할 수 있습니다. (클래스: 동물 / 객체: 호랑이, 강아지)

## Object (객체)
- 객체는 세상에 존재하는 유일무이한 사물입니다.

## Constructor (생성자)
- 생성자를 통해 객체를 생성할 때 데이터를 넣어주거나, 내부적으로 원하는 행동을 실행할 수 있습니다.
- 생성자는 생성 시에 호출되는 함수입니다.
- 파이썬에서 생성자 함수의 이름은 `__init__` 으로 고정돼 있습니다. 무조건 생성자 이름의 함수는 `__init__` 입니다.


```python
class Person:
    def __init__(self):
        print("Hi I am created", self)

person_1 = Person()
person_2 = Person()
```
- `self`: 객체 자기 자신을 가리킵니다. 파라미터를 따로 넣어줄 필요 없이, 호출만 하면 self에 객체 자기 자신에 대한 정보를 넣습니다.



- 다음의 예시처럼, `self`를 사용해, 객체에 데이터를 쌓을 수 있습니다.
- `self.name`에 `parm_name`을 저장하는 것은 해당 객체의 `name`이라는 변수에 저장된다는 의미입니다.
```python
class Person:
  def __init__(self, pram_name):
    print("Hi I am created", self)
    self.name = pram_name

person1 = Person("my_name1")
print(person1.name)

person2 = Person("my_name2")
print(person2.name)
```

## Method (메소드)
- 클래스 내부의 함수를 Method(메소드)라고 부릅니다.
- 각 객체의 변수를 사용해서 메소드를 구현할 수 있습니다.

```python
class Person:
  def __init__(self, pram_name):
    print("Hi I am created", self)
    self.name = pram_name
  
  def talk(self):
    print("안녕하세요. 저는", self.name, "입니다.")

person1 = Person("my_name1")
print(person1.name)
person1.talk()

person2 = Person("my_name2")
print(person2.name)
person2.talk()
```

## 정리
이처럼 클래스를 이용하면 연관성 있는 데이터들을 클래스 내에서 관리 가능하며,
다양한 객체들을 쉽게 생성할 수 있습니다.