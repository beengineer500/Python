# 1. 알파벳별 빈도를 매긴다. 
# 2. 빈도가 1인 알파벳을 뽑는다. (빈도 수가 1인 알파벳이 없다면, _ 를 반환환다.)
# 3. 문자열의 처음부터 인덱스의 값과 빈도수가 1인 알파벳이 일치하는 지 비교한다.
# 4. 일치할 경우 해당 알파벳을 반환한다.

input = "abadabac"

def find_not_repeating_first_character(string):
  # 시간 복잡도 : O(N)
  occurrence_array = find_occurred_alphabet(string)
  not_repeating_character_array = []
  # 시간 복잡도 : 26 (상수)
  for index in range(len(occurrence_array)):
      alphabet_occurrence = occurrence_array[index]
      if alphabet_occurrence == 1:
        not_repeating_character_array.append(chr(index + ord('a')))

  # 시간 복잡도 : O(N)
  for char in string:
    if char in not_repeating_character_array:
      return char

  return "_"


def find_occurred_alphabet(string):
  alphabet_occurrence_array = [0] * 26

  for char in string:
    if not char.isalpha():
      continue
    arr_index = ord(char) - ord('a')
    alphabet_occurrence_array[arr_index] += 1

  return alphabet_occurrence_array


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))