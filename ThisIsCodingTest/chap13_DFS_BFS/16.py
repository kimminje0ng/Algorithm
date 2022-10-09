# https://www.acmicpc.net/problem/14502

# n:세로, m:가로
# 0:빈칸, 1:벽, 2:바이러스
n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))
#print(lab)

# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tmp = [[0] * m for _ in range(n)]
result = 0  # 남은 공간

# 빈칸 세는 함수
def count_blank():
    blank = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                blank += 1
    return blank

def move_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                move_virus(nx, ny)

def dfs(count):
    global result

    # 울타리 3개 설치되면 => 전파 시작
    if count == 3:
        # 세팅 복사
        for i in range(n):
            for j in range(m):
                tmp[i][j] = lab[i][j]
        # 전파 시작
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    move_virus(i,j)
        result =  max(result, count_blank())
        return
    
    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1

dfs(0)
print(result)