user_num1, user_num2 = map(int, input().split())

a = max(user_num1, user_num2)
b = min(user_num1, user_num2)

while(b != 0):
    a, b = b, a%b

print(a) 
print(int(user_num1*user_num2 / a))
