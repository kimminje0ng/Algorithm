# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())

city_map = []
chiken = []
home = []

for x in range(n):
    city_map.append(list(map(int, input().split())))
    for y in range(n):
        if city_map[x][y] == 1:
            home.append([x, y])
        if city_map[x][y] == 2:
            chiken.append([x, y])
#print(city_map)
#print(home)
#print(chiken)

# 치킨 조합
chiken_combs = list(combinations(chiken, m))

result = [] # 조합 별로 최소 도시 치킨 거리 저장
for comb in chiken_combs:
    sum_dist = 0
    for ho_x, ho_y in home:
        min_dist = 1e9
        for ch_x, ch_y in comb:
            min_dist = min(min_dist, abs(ch_x - ho_x) + abs(ch_y - ho_y))
        sum_dist += min_dist
    result.append(sum_dist)

#print(result)
print(min(result))