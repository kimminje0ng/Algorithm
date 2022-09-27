# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# key를 시계방향으로 90도 회전하는 함수
def turn_clockwise(before):
    n = len(before)
    after = [[0] * n for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            after[y][n-x-1] = before[x][y]
            
    return after

# 원래의 lock 배열이 모두 1으로 구성되었는지 확인하는 함수
def check(lock):
    n = len(lock) // 3
    for y in range(n, n+n):
        for x in range(n, n+n):
            if lock[x][y] != 1: # 만약 1이 아닌게 있으면 바로 break
                return False
    return True


def solution(key, lock):
    n = len(lock)   # lock size
    m = len(key)    # key size
    
    # 자물쇠 크기 늘림
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    
    # 늘린 자물쇠로 옮기기
    for y in range(n):
        for x in range(n):
            new_lock[x+n][y+n] = lock[x][y]

    # 원래 lock이 true일 경우
    if check(new_lock) == True:
        return True
    
    # 90도씩 회전    
    for rotation in range(4):
        for y in range(1,n*2):        # 자물쇠
            for x in range(1,n*2):
                for key_y in range(m): # key
                    for key_x in range(m):
                        new_lock[x + key_x][y + key_y] += key[key_x][key_y]
                
                # key가 맞으면 True
                if check(new_lock) == True:
                    return True
                
                for key_y in range(m): # key
                    for key_x in range(m):
                        new_lock[x + key_x][y + key_y] -= key[key_x][key_y]
        
        key = turn_clockwise(key)   # 키 회전

    return False