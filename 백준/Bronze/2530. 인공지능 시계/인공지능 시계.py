A, B, C = map(int, input().split())
D = int(input())


input_time = A * 3600 + B * 60 + C
total_time = input_time + D

total_hour = (total_time // 3600) % 24
total_min = (total_time % 3600) // 60
total_sec = total_time % 60

print(total_hour, total_min, total_sec)