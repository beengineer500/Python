# Q. 문자열을 받았을 때, 가장 많이 등장한 알파벳 찾기

# 방법 1. a, b, c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 한다.

def find_occurred_alphbet_1(string):
  max_occurrence = 0
  max_alphabet = alphabet_array[0]

  for alphabet in alphabet_array:
    occuerrence = 0

    for char in string:
      if char == alphabet:
        occurence += 1
    
    if occurrence > max_occurrence:
      max_alphabet = alphabet
      max_occurrence = occurrence

  return max_alphabet

def find_alpha_occurrenc_array(string):
  alphabet_occurrnece_array = [0] * 26
  for char in string:
    if not char.isalpha():
      continue
  
    arr_index = ord(char) - ord('a')
    alphabet_occurrnece_array[arr_index] += 1

  return alphabet_occurrnece_array


# 방법2

# 1) 문자열을 받는다.
# 2) 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인데스와 시켜서 알파벳의 빈도수를 업데이트 한다.


def find_occurred_alphabet_2(string):
  alphabet_occurrence_array = [0] * 26

  for char in string:
    if not char.isalpha():
      continue
    arr_index = ord(char) - ord('a')
    alphabet_occurrence_array[arr_index] += 1
  
  max_occurrence = 0
  max_alphabet_index = 0

  for index in range(len(alphabet_occurrence_array)):
    alphabet_occurrence = alphabet_occurrence_array[index]

    if alphabet_occurrence > max_occurrence:
      max_occurrence = alphabet_occurrence
      max_alphabet_index = index    

  return chr(max_alphabet_index + ord('a'))



print(find_occurred_alphabet_2("123aaaaaaaaabdec"))
print(find_occurred_alphabet_2("123abdbbbbbbbbec"))
print(find_occurred_alphabet_2("123aaaaaaaaabdeccccccccccccccccccc"))
print(find_occurred_alphabet_2("123aaaaaaaaabdec"))
