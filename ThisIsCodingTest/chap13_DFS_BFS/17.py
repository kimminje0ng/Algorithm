# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

info = []   # map 정보
virus = []  # virus 정보

# map 정보 입력
for i in range(n):
    info.append(list(map(int, input().split())))
    for j in range(n):
        if info[i][j] != 0:
            virus.append([info[i][j], 0, i, j]) # virus종류, 시간, x, y
#print(info)
#print(virus)

# virus는 낮은 것부터 전염됨
virus.sort() 
q = deque(virus)

# result 조건 입력
target_s, target_x, target_y = map(int, input().split())

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while q:
    virus_type, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if info[nx][ny] == 0:
                info[nx][ny] = virus_type
                q.append([virus_type, s+1, nx, ny])
    #print(info)

# result 출력(좌표 0부터 시작)
print(info[target_x-1][target_y-1])