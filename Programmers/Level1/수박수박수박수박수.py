# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i%2 != 0:
            answer += '수'
        else:
            answer += '박'
    return answer

# 풀이2
def solution(n):
    answer = '수박' * (n//2)
    if n%2 != 0:
        answer += '수'
    return answer

# 다른 사람 풀이 -> if문 안쓰고 한 번에 바로 return
def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)