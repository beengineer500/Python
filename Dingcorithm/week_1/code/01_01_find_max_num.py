def my_find_max_num(array):
  max_num = 0
  for i in array:
    if i >= max_num:
      max_num = i
  return max_num


def find_max_num1(array):
  for number in array:
    is_max_num = True
    for compare_number in array:
      if number < compare_number:
        is_max_num = False
    if is_max_num:
      return number


print("정답 = 6 / 현재 풀이 값 = ", my_find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", my_find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", my_find_max_num([6, 9, 2, 7, 1888]))

