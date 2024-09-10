### 하나하나 비교하는 것이 아니라 중심을 기준으로 수를 하나씩 증가 혹은 감소해가며 소수인지 아닌지 판별 

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

int_change = int(input()) 

for _ in range(int_change):
    input_num = int(input())
    
    plus_num = input_num // 2 # 하나씩 증가하면서 확인할 숫자 
    minus_num = input_num // 2 # 하나씩 감소시키면서 확인할 숫자 
    
    
    for _ in range(input_num // 2):
        if (is_prime(plus_num) & is_prime(minus_num)):
            print(minus_num, plus_num)
            break
        else:
            plus_num += 1
            minus_num -= 1