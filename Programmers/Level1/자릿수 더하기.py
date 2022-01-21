# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = sum(map(int, str(n)))
    return answer


# 다른 풀이 : 재귀 함수
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)