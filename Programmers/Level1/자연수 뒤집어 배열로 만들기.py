# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = list(map(int,str(n)))
    answer.reverse()  # 배열 거꾸로
    return answer


# 다른 풀이 - reversed를 list() 밖에 하면 null 반한됨..
def digit_reverse(n):
    return list(map(int, reversed(str(n))))