# https://www.acmicpc.net/problem/18405

n, k = map(int, input().split())

info = []
for i in range(n):
    info.append(list(map(int, input().split())))
print(info)

virus = []
for i in range(n):
    for j in range(n):
        if info[i][j] != 0:
            virus.append([info[i][j], 0, i, j])

s, x, y = map(int, input().split())

def move_virus(virus_num, info):
    new_info = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if info[i][j] == virus_num:
                new_info[i][j] = virus_num
                if i-1 >= 0 and info[i-1][j] == 0:  # 상
                    new_info[i-1][j] = virus_num
                if i+1 < n and info[i+1][j] == 0: # 하
                    new_info[i+1][j] = virus_num
                if j-1 >= 0 and info[i][j-1] == 0:# 좌
                    new_info[i][j-1] = virus_num
                if j+1 < n and info[i][j+1] == 0: # 우
                    new_info[i][j+1] = virus_num
    return new_info

time = 0
while(time <= s):
    for virus_num in range(1,k):
        # 이렇게 해보니까 바로 info에 새로운 virus가 업데이트돼서 문제 발생함.
        info = move_virus(virus_num, info)
        print(info)
    time += 1


print(info[x-1][y-1])