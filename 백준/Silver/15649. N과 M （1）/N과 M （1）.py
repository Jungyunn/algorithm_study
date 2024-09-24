from itertools import permutations

n, m = map(int, input().split())
num_list = list(range(1, n+1))

num_perm = permutations(num_list, m)
for perm in num_perm:
    print(*perm)