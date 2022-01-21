# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    time = 0
    while num != 1:
        if num % 2 == 0 :
            num = num / 2
        else:
            num = num * 3 + 1
        time += 1
        if time == 500:  # 501인 것 같음..
            return -1
    return time


## 다른 풀이
def solution(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1