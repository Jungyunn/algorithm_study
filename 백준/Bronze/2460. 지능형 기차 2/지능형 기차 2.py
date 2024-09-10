total_num = 0
p_per_station = []
for s_idx in range(10):
    out_num, in_num = map(int, input().split())
    total_num = total_num - out_num + in_num
    p_per_station.append(total_num)

print(max(p_per_station))