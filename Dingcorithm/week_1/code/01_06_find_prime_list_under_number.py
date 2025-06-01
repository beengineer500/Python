# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

# 소수 : 1과 자기 자신으로만 나눠지는 수

# 1. input > 0인지 확인한다.
# 2. 2 ~ input 구간을 반복한다.
# 3. 각 반복인 n마다 2 ~ n-1 구간을 반복하며, 소수로 나누어 떨어지는 지 확인한다. 나눠떨어지면 그 수는 소수가 아니다. (반복문 종료)
# 3-1. 2, 3으로 나뉜다면 2와 3의 곱셈으로 표현할 수 있는 수들로도 나눠진다. 따라서, 해당 숫자보다 낮은 소수들로만 점검을 하면 효율적으로 구할 수 있다.
# 4. 안나눠지는 수는 소수이므로, 리스트에 넣는다.

# (개선) 소수의 특징 : N의 제곱근보다 작은 어떤 소수로도 나눠떨어지지 않는다.
# N의 제곱근보다 작은 소수로 나눠떨어진다면, 소수가 아니다. : i * i <= n 조건 추가

input = 20

def find_prime_list_under_number(number):
    if number > 0:
        
        prime_list = []

        # 2 ~ number 구간에서 소수를 확인한다.
        for n in range(2, number + 1):
            # 각 수별로, 2 ~ 수-1 구간에서 소수로 나눠지는지 점검한다. 
            for i in prime_list:
                if i * i  <= n and n % i == 0:
                    break
            else:
                prime_list.append(n)
    else:
        print("입력 값은 양의 정수여야 합니다. 다시 입력하세요.")
    return prime_list       

result = find_prime_list_under_number(input)
print(result)