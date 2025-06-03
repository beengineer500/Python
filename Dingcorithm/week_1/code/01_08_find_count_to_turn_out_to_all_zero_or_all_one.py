input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == "0":
        count_to_all_one += 1
    if string[0] == "1":
        count_to_all_zero += 1

    for i in range(len(string) - 1): # i : 0 ~ 문자열의 길이 - 2 까지의 범위를 가진다.
        if string[i] != string[i + 1]: # 현재 인덱스의 문자와 다음 인덱스의 문자가 다를 경우
            if string[i + 1] == "1":
                count_to_all_zero += 1
            if string[i + 1] == "0":
                count_to_all_one += 1

    print(count_to_all_zero, count_to_all_one)
    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)