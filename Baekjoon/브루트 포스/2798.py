from itertools import combinations

N, M = map(int, input().split())
card_num = list(map(int, input().split()))
# print(card_num)

perm = list(combinations(card_num, 3))
# print(perm)

max_sum = 0
for p in perm:
    if max_sum < sum(p) and sum(p) <= M:
        max_sum = sum(p)

print(max_sum)