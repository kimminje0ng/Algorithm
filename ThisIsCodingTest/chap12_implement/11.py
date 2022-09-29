# https://www.acmicpc.net/problem/3190
# board 정보 : 0(없음), 1(사과), 2(뱀)

## map 생성
n = int(input())    # 보드 사이즈 n
board = [[0 for col in range(n)] for row in range(n)]

## map(사과) 정보 입력
k = int(input())    # 사과 위치. 3 4
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

## 방향 전환 정보 입력 
l = int(input())    # 뱀 방향 정보. 3 D
change_direction = ['0' for col in range(l)]
for _ in range(l):
    time, dir = input().split()
    change_direction.append((int(x), dir))

## ['R', 'D', 'L', 'U']. 시작: R(동)
# 시계방향 회전. (x,y) -> (x,y+1)
#              (x+1, y)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]           

## 회전
def turn(turn_way, direction):
    if turn_way == 'L':
        direction = (direction - 1) % 4
    elif turn_way == 'D':
        direction = (direction + 1) % 4
    return direction

## main 코드
def simulate():
    x, y = 0, 0     # 뱀 머리 위치
    board[x][y] = 2 # 뱀 존재하면 board=2
    direction = 0   # 시작은 R(동) 방향
    time = 0        # 실행 시간
    next_direction = 0       # 다음 회전 정보

    q = [(x, y)]    # 뱀의 위치 정보(꼬리가 맨 앞, 머리가 맨 뒤)

    while (True):
        nx = x + dx[direction]  # 다음 위치 정보
        ny = y + dy[direction]

        if nx >= 0 and nx <= (n-1) and ny >= 0 and ny <= (n-1):
            # 맵에 아무것도 없으면 뱀 이동
            if board[nx][ny] == 0:   
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)   # 이전 값(previous x)
                board[px][py] = 0
            # 맵에 사과가 있으면 꼬리 그대로
            elif board[nx][ny] == 1:    
                board[nx][ny] = 2
                q.append((nx, ny))
            # 몸통이나 벽이면 종료
            else:
                time += 1
                break
            
            # 종료되지 않았으면 위치 저장
            x, y = nx, ny
            time += 1

            ## 회전할 시간이 되면 회전. l = 방향 전환 횟수
            if next_direction < l and time == change_direction[next_direction][0]:
                direction = turn(direction, change_direction[next_direction][1])
                next_direction += 1
        
        return time


print(simulate())