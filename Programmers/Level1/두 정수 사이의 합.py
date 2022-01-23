# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a > b: a,b = b,a
    answer = sum(i for i in range(a,b+1))
    return answer

# 간단한 풀이
def solution(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))  # 바로 range사용 가능

# 수학 공식(|a-b|+1*(a+b)/2)
def solution(a, b):
    return (abs(a-b) + 1) * (a+b) // 2