# 빅오 : 최악의 경우
# 빅오메가 : 최선의 경우


 

def is_number_exist(number, array):
  for i in array:    # array의 길이만큼 연산 수행
  if number == i:    # 비교 연산 1번
    retrun True  
  return False

print("정답 = True 현재 풀이 값 :", is_number_exist(3, [3, 5, 6, 1, 2, 4]))  # 운이 좋은 경우, 시간 복잡도가 1밖에 안걸린다.
print("정답 = True 현재 풀이 값 :", is_number_exist(7 [6, 6, 6]))
print("정답 = True 현재 풀이 값 :", is_number_exist(2, [6, 9, 2, 7, 1888])) # 운이 안좋은 경우   