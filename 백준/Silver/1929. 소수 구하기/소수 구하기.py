import math

start_num, end_num = map(int, input().split())
result = []

for tmp_num in range(start_num, end_num + 1):
    if tmp_num < 2:  # 1과 0은 소수가 아님
        continue
    for num in range(2, int(math.sqrt(tmp_num)) + 1):  # 제곱근까지만 검사
        if tmp_num % num == 0:
            break
    else:
        print(tmp_num)
