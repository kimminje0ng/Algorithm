# https://www.acmicpc.net/problem/18352

from collections import deque

# 정보 입력
city_num, road_num, MIN_DISTANCE, start_city = map(int, input().split())

# 도로 정보 입력. city는 1~N
graph = [[] for _ in range(city_num + 1)]
for _ in range(road_num):
    a, b = map(int, input().split())
    graph[a].append(b)

# distance 변수
distance = [-1] * (city_num + 1)
distance[start_city] = 0

# DFS 계산
q = deque([start_city])
while q:
    now_city = q.popleft()
    for next_node in graph[now_city]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now_city] + 1
            q.append(next_node)

# Min Distance 가진 city 출력
flag = False
for i in range(1, city_num + 1):
    if distance[i] == MIN_DISTANCE:
        print(i)
        flag = True

if flag == False:
    print(-1)

